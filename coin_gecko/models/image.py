from dataclasses import dataclass
from typing import Optional, Any, List, Dict, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser

from coin_gecko.util import from_union, from_str, from_none


@dataclass
class Image:
    thumb: Optional[str] = None
    small: Optional[str] = None
    large: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        thumb = from_union([from_str, from_none], obj.get("thumb"))
        small = from_union([from_str, from_none], obj.get("small"))
        large = from_union([from_str, from_none], obj.get("large"))
        return Image(thumb, small, large)

    def to_dict(self) -> dict:

        result: dict = {}
        result["thumb"] = from_union([from_str, from_none], self.thumb)
        result["small"] = from_union([from_str, from_none], self.small)
        result["large"] = from_union([from_str, from_none], self.large)
        return result

