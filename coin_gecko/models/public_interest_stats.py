from dataclasses import dataclass
from typing import Any

from coin_gecko.util import from_none


@dataclass
class PublicInterestStats:
    alexa_rank: None
    bing_matches: None

    @staticmethod
    def from_dict(obj: Any) -> 'PublicInterestStats':
        assert isinstance(obj, dict)
        alexa_rank = from_none(obj.get("alexa_rank"))
        bing_matches = from_none(obj.get("bing_matches"))
        return PublicInterestStats(alexa_rank, bing_matches)

    def to_dict(self) -> dict:
        result: dict = {"alexa_rank": from_none(self.alexa_rank), "bing_matches": from_none(self.bing_matches)}
        return result
