import logging
from typing import Dict, Callable, Any

logger = logging.getLogger(__name__)

class MCPToolRegistry:
    """
    Model Context Protocol (MCP) Standardized Registry.
    Provides a universal, secure interface for LLMs to discover and execute 
    enterprise B2B tools dynamically, abstracting away the underlying API logic.
    """
    def __init__(self):
        self._tools: Dict[str, dict] = {}

    def register_tool(self, name: str, description: str, schema: dict, func: Callable):
        self._tools[name] = {
            "description": description,
            "schema": schema,
            "executable": func
        }
        logger.info(f"MCP Tool Registered: {name}")

    def get_tool_manifest(self) -> list:
        return [
            {"name": name, "description": data["description"], "parameters": data["schema"]}
            for name, data in self._tools.items()
        ]

    def execute_tool(self, tool_name: str, **kwargs) -> Any:
        if tool_name not in self._tools:
            logger.error(f"MCP Execution Failed: Tool '{tool_name}' not found.")
            raise ValueError(f"Unregistered tool: {tool_name}")
            
        logger.info(f"Executing MCP Tool: {tool_name}")
        return self._tools[tool_name]["executable"](**kwargs)
