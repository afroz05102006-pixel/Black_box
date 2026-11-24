from enum import Enum

class Provenance(Enum):
    GREEN = "trusted"
    RED = "untrusted"
    BOTH = "mixed"
    UNKNOWN = "unknown"
