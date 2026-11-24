from typing import Any
from .provenance import Provenance

class Guard:
    def check(self, tool_name: str, args: dict, provenance: Provenance) -> str:
        """Decide: ALLOW, HOLD, or BLOCK"""
        if tool_name in ["read_inbox", "list_events"]:
            return "ALLOW"
        
        if provenance == Provenance.RED and tool_name in ["send_email", "pay", "delete"]:
            return "BLOCK"
            
        return "HOLD"
