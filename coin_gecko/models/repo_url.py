from dataclasses import dataclass
from typing import Optional, Any, List

from coin_gecko.util import from_union, from_list, from_str, from_none


@dataclass
class ReposURL:
    github: Optional[List[str]] = None
    bitbucket: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ReposURL':
        assert isinstance(obj, dict)
        github = from_union([lambda x: from_list(from_str, x), from_none], obj.get("github"))
        bitbucket = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("bitbucket"))
        return ReposURL(github, bitbucket)

    def to_dict(self) -> dict:
        result: dict = {}
        result["github"] = from_union([lambda x: from_list(from_str, x), from_none], self.github)
        result["bitbucket"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.bitbucket)
        return result
