from dataclasses import dataclass
from typing import Any, Dict
from datetime import datetime

from coin_gecko.models.market import Market
from coin_gecko.util import from_str, from_float, from_dict, from_datetime, from_bool, from_none, to_class, to_float


@dataclass
class PricePair:
    base: str
    target: str
    market: Market
    last: float
    volume: float
    converted_last: Dict[str, float]
    converted_volume: Dict[str, float]
    trust_score: str
    bid_ask_spread_percentage: float
    timestamp: datetime
    last_traded_at: datetime
    last_fetch_at: datetime
    is_anomaly: bool
    is_stale: bool
    trade_url: str
    token_info_url: None
    coin_id: str
    target_coin_id: str

    @staticmethod
    def from_dict(obj: Any) -> 'PricePair':
        assert isinstance(obj, dict)
        base = from_str(obj.get("base"))
        target = from_str(obj.get("target"))
        market = Market.from_dict(obj.get("market"))
        last = from_float(obj.get("last"))
        volume = from_float(obj.get("volume"))
        converted_last = from_dict(from_float, obj.get("converted_last"))
        converted_volume = from_dict(from_float, obj.get("converted_volume"))
        trust_score = from_str(obj.get("trust_score"))
        bid_ask_spread_percentage = from_float(obj.get("bid_ask_spread_percentage"))
        timestamp = from_datetime(obj.get("timestamp"))
        last_traded_at = from_datetime(obj.get("last_traded_at"))
        last_fetch_at = from_datetime(obj.get("last_fetch_at"))
        is_anomaly = from_bool(obj.get("is_anomaly"))
        is_stale = from_bool(obj.get("is_stale"))
        trade_url = from_str(obj.get("trade_url"))
        token_info_url = from_none(obj.get("token_info_url"))
        coin_id = from_str(obj.get("coin_id"))
        target_coin_id = from_str(obj.get("target_coin_id"))
        return PricePair(base,
                         target,
                         market,
                         last,
                         volume,
                         converted_last,
                         converted_volume,
                         trust_score,
                         bid_ask_spread_percentage,
                         timestamp,
                         last_traded_at,
                         last_fetch_at,
                         is_anomaly,
                         is_stale,
                         trade_url,
                         token_info_url,
                         coin_id,
                         target_coin_id
                         )

    def to_dict(self) -> dict:
        result: dict = {"base": from_str(self.base), "target": from_str(self.target),
                        "market": to_class(Market, self.market), "last": to_float(self.last),
                        "volume": to_float(self.volume), "converted_last": from_dict(to_float, self.converted_last),
                        "converted_volume": from_dict(to_float, self.converted_volume),
                        "trust_score": from_str(self.trust_score),
                        "bid_ask_spread_percentage": to_float(self.bid_ask_spread_percentage),
                        "timestamp": self.timestamp.isoformat(), "last_traded_at": self.last_traded_at.isoformat(),
                        "last_fetch_at": self.last_fetch_at.isoformat(), "is_anomaly": from_bool(self.is_anomaly),
                        "is_stale": from_bool(self.is_stale), "trade_url": from_str(self.trade_url),
                        "token_info_url": from_none(self.token_info_url), "coin_id": from_str(self.coin_id),
                        "target_coin_id": from_str(self.target_coin_id)}
        return result
