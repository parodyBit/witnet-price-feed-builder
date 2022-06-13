from dataclasses import dataclass
from typing import Any

from coin_gecko.util import from_str, from_bool


@dataclass
class Market:
    name: str
    identifier: str
    has_trading_incentive: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Market':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        identifier = from_str(obj.get("identifier"))
        has_trading_incentive = from_bool(obj.get("has_trading_incentive"))
        return Market(name, identifier, has_trading_incentive)

    def to_dict(self) -> dict:
        result: dict = {"name": from_str(self.name), "identifier": from_str(self.identifier),
                        "has_trading_incentive": from_bool(self.has_trading_incentive)}
        return result
