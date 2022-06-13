from dataclasses import dataclass
from typing import Optional, Any, Dict
from datetime import datetime

from coin_gecko.models.market import Market
from coin_gecko.util import from_none, from_str, from_union, from_float, from_dict, from_datetime, from_bool,\
    to_float, to_class


@dataclass
class Ticker:
    token_info_url: None
    base: Optional[str] = None
    target: Optional[str] = None
    market: Optional[Market] = None
    last: Optional[float] = None
    volume: Optional[float] = None
    converted_last: Optional[Dict[str, float]] = None
    converted_volume: Optional[Dict[str, float]] = None
    trust_score: Optional[str] = None
    bid_ask_spread_percentage: Optional[float] = None
    timestamp: Optional[datetime] = None
    last_traded_at: Optional[datetime] = None
    last_fetch_at: Optional[datetime] = None
    is_anomaly: Optional[bool] = None
    is_stale: Optional[bool] = None
    trade_url: Optional[str] = None
    coin_id: Optional[str] = None
    target_coin_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Ticker':
        assert isinstance(obj, dict)
        token_info_url = from_none(obj.get("token_info_url"))
        base = from_union([from_str, from_none], obj.get("base"))
        target = from_union([from_str, from_none], obj.get("target"))
        market = from_union([Market.from_dict, from_none], obj.get("market"))
        last = from_union([from_float, from_none], obj.get("last"))
        volume = from_union([from_float, from_none], obj.get("volume"))
        converted_last = from_union([lambda x: from_dict(from_float, x), from_none], obj.get("converted_last"))
        converted_volume = from_union([lambda x: from_dict(from_float, x), from_none], obj.get("converted_volume"))
        trust_score = from_union([from_str, from_none], obj.get("trust_score"))
        bid_ask_spread_percentage = from_union([from_float, from_none], obj.get("bid_ask_spread_percentage"))
        timestamp = from_union([from_datetime, from_none], obj.get("timestamp"))
        last_traded_at = from_union([from_datetime, from_none], obj.get("last_traded_at"))
        last_fetch_at = from_union([from_datetime, from_none], obj.get("last_fetch_at"))
        is_anomaly = from_union([from_bool, from_none], obj.get("is_anomaly"))
        is_stale = from_union([from_bool, from_none], obj.get("is_stale"))
        trade_url = from_union([from_str, from_none], obj.get("trade_url"))
        coin_id = from_union([from_str, from_none], obj.get("coin_id"))
        target_coin_id = from_union([from_str, from_none], obj.get("target_coin_id"))
        return Ticker(token_info_url,
                      base,
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
                      coin_id,
                      target_coin_id
                      )

    def to_dict(self) -> dict:
        result: dict = {"token_info_url": from_none(self.token_info_url),
                        "base": from_union([from_str, from_none], self.base),
                        "target": from_union([from_str, from_none], self.target),
                        "market": from_union([lambda x: to_class(Market, x), from_none], self.market),
                        "last": from_union([to_float, from_none], self.last),
                        "volume": from_union([to_float, from_none], self.volume),
                        "converted_last": from_union([lambda x: from_dict(to_float, x), from_none],
                                                     self.converted_last),
                        "converted_volume": from_union([lambda x: from_dict(to_float, x), from_none],
                                                       self.converted_volume),
                        "trust_score": from_union([from_str, from_none], self.trust_score),
                        "bid_ask_spread_percentage": from_union([to_float, from_none], self.bid_ask_spread_percentage),
                        "timestamp": from_union([lambda x: x.isoformat(), from_none], self.timestamp),
                        "last_traded_at": from_union([lambda x: x.isoformat(), from_none], self.last_traded_at),
                        "last_fetch_at": from_union([lambda x: x.isoformat(), from_none], self.last_fetch_at),
                        "is_anomaly": from_union([from_bool, from_none], self.is_anomaly),
                        "is_stale": from_union([from_bool, from_none], self.is_stale),
                        "trade_url": from_union([from_str, from_none], self.trade_url),
                        "coin_id": from_union([from_str, from_none], self.coin_id),
                        "target_coin_id": from_union([from_str, from_none], self.target_coin_id)}
        return result
