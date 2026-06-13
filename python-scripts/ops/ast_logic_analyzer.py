import ast
import logging
import json

class ASTLogicAnalyzer:
    def __init__(self):
        self.risk_patterns = ['while True', 'eval(', 'exec(']

    def analyze_source_dry_run(self, file_path: str, source_code: str) -> dict:
        logging.info(f"[PORTFOLIO MOCK] Parsing AST for: {file_path}")
        
        try:
            tree = ast.parse(source_code)
            node_count = sum(1 for _ in ast.walk(tree))
            
            risk_score = 0
            for pattern in self.risk_patterns:
                if pattern in source_code:
                    risk_score += 50
                    logging.warning(f"[SECOPS MOCK] High-risk pattern detected: {pattern}")

            logging.info(f"[SRE MOCK] AST parsed successfully. Nodes analyzed: {node_count}")
            
            return {
                "file": file_path,
                "complexity_nodes": node_count,
                "security_risk_score": risk_score,
                "status": "REJECTED" if risk_score > 0 else "APPROVED"
            }
        except SyntaxError as e:
            logging.critical(f"[FATAL] Syntax invalid. AST parsing failed: {e}")
            return {"status": "ERROR"}
