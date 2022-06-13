from dataclasses import dataclass
from typing import Optional, Any, List, Dict, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser

from coin_gecko.util import from_union, from_int, from_none


@dataclass
class CodeAdditionsDeletions4_Weeks:
    additions: Optional[int] = None
    deletions: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CodeAdditionsDeletions4_Weeks':
        assert isinstance(obj, dict)
        additions = from_union([from_int, from_none], obj.get("additions"))
        deletions = from_union([from_int, from_none], obj.get("deletions"))
        return CodeAdditionsDeletions4_Weeks(additions, deletions)

    def to_dict(self) -> dict:
        result: dict = {"additions": from_union([from_int, from_none], self.additions),
                        "deletions": from_union([from_int, from_none], self.deletions)}
        return result
