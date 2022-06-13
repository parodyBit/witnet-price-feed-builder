from dataclasses import dataclass
from typing import Optional, Any

from coin_gecko.util import from_union, from_str, from_none


@dataclass
class Platforms:
    empty: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Platforms':
        assert isinstance(obj, dict)
        empty = from_union([from_str, from_none], obj.get(""))
        return Platforms(empty)

    def to_dict(self) -> dict:
        result: dict = {"": from_union([from_str, from_none], self.empty)}
        return result
