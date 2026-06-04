import sqlite3
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

class StatefulGraphRAGExtractor:
    """
    Enterprise GraphRAG Architecture.
    Extracts entities (Organizations, Decision Makers) and their relationships 
    from unstructured B2B data. Maintains a stateful local graph database 
    to prevent duplicate entity creation and map complex corporate networks.
    """
    def __init__(self, db_path: str = "b2b_knowledge_graph.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS entities 
                             (entity_id TEXT PRIMARY KEY, type TEXT, name TEXT)''')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS relationships 
                             (source_id TEXT, target_id TEXT, relation_type TEXT,
                             PRIMARY KEY (source_id, target_id, relation_type))''')

    def inject_graph_nodes(self, entities: List[Dict[str, str]], relationships: List[Dict[str, str]]):
        logger.info(f"Injecting {len(entities)} entities into the stateful GraphRAG schema.")
        
        for entity in entities:
            self.conn.execute("INSERT OR IGNORE INTO entities (entity_id, type, name) VALUES (?, ?, ?)",
                              (entity["id"], entity["type"], entity["name"]))
            
        for rel in relationships:
            self.conn.execute("INSERT OR IGNORE INTO relationships (source_id, target_id, relation_type) VALUES (?, ?, ?)",
                              (rel["source"], rel["target"], rel["relation"]))
            
        self.conn.commit()
        logger.debug("Graph topology successfully updated. Zero duplicate nodes created.")
