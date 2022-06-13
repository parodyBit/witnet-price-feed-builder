from dataclasses import dataclass
from typing import Optional, Any, List, Dict, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser

from coin_gecko.util import from_union, from_str, from_none


@dataclass
class Description:
    en: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Description':
        assert isinstance(obj, dict)
        en = from_union([from_str, from_none], obj.get("en"))
        return Description(en)

    def to_dict(self) -> dict:
        result: dict = {"en": from_union([from_str, from_none], self.en)}
        return result
