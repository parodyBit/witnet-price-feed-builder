
from dataclasses import dataclass
from typing import Optional, Any, List
from datetime import datetime

from coin_gecko.models.community_data import CommunityData
from coin_gecko.models.description import Description
from coin_gecko.models.developer_data import DeveloperData
from coin_gecko.models.image import Image
from coin_gecko.models.links import Links
from coin_gecko.models.platforms import Platforms
from coin_gecko.models.public_interest_stats import PublicInterestStats
from coin_gecko.models.ticker import Ticker
from coin_gecko.util import from_none, from_union, from_list, from_str, from_int, from_float, from_datetime, to_class, \
    to_float


@dataclass
class Coin:
    asset_platform_id: None
    hashing_algorithm: None
    public_notice: None
    genesis_date: None
    sentiment_votes_up_percentage: None
    sentiment_votes_down_percentage: None
    id: Optional[str] = None
    symbol: Optional[str] = None
    name: Optional[str] = None
    platforms: Optional[Platforms] = None
    block_time_in_minutes: Optional[int] = None
    categories: Optional[List[str]] = None
    additional_notices: Optional[List[Any]] = None
    description: Optional[Description] = None
    links: Optional[Links] = None
    image: Optional[Image] = None
    country_origin: Optional[str] = None
    market_cap_rank: Optional[int] = None
    coingecko_rank: Optional[int] = None
    coingecko_score: Optional[float] = None
    developer_score: Optional[float] = None
    community_score: Optional[float] = None
    liquidity_score: Optional[float] = None
    public_interest_score: Optional[int] = None
    community_data: Optional[CommunityData] = None
    developer_data: Optional[DeveloperData] = None
    public_interest_stats: Optional[PublicInterestStats] = None
    status_updates: Optional[List[Any]] = None
    last_updated: Optional[datetime] = None
    tickers: Optional[List[Ticker]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Coin':
        assert isinstance(obj, dict)
        asset_platform_id = from_none(obj.get("asset_platform_id"))
        hashing_algorithm = from_none(obj.get("hashing_algorithm"))
        public_notice = from_none(obj.get("public_notice"))
        genesis_date = from_none(obj.get("genesis_date"))
        sentiment_votes_up_percentage = from_none(obj.get("sentiment_votes_up_percentage"))
        sentiment_votes_down_percentage = from_none(obj.get("sentiment_votes_down_percentage"))
        id = from_union([from_str, from_none], obj.get("id"))
        symbol = from_union([from_str, from_none], obj.get("symbol"))
        name = from_union([from_str, from_none], obj.get("name"))
        platforms = from_union([Platforms.from_dict, from_none], obj.get("platforms"))
        block_time_in_minutes = from_union([from_int, from_none], obj.get("block_time_in_minutes"))
        categories = from_union([lambda x: from_list(from_str, x), from_none], obj.get("categories"))
        additional_notices = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("additional_notices"))
        description = from_union([Description.from_dict, from_none], obj.get("description"))
        links = from_union([Links.from_dict, from_none], obj.get("links"))
        image = from_union([Image.from_dict, from_none], obj.get("image"))
        country_origin = from_union([from_str, from_none], obj.get("country_origin"))
        market_cap_rank = from_union([from_int, from_none], obj.get("market_cap_rank"))
        coingecko_rank = from_union([from_int, from_none], obj.get("coingecko_rank"))
        coingecko_score = from_union([from_float, from_none], obj.get("coingecko_score"))
        developer_score = from_union([from_float, from_none], obj.get("developer_score"))
        community_score = from_union([from_float, from_none], obj.get("community_score"))
        liquidity_score = from_union([from_float, from_none], obj.get("liquidity_score"))
        public_interest_score = from_union([from_int, from_none], obj.get("public_interest_score"))
        community_data = from_union([CommunityData.from_dict, from_none], obj.get("community_data"))
        developer_data = from_union([DeveloperData.from_dict, from_none], obj.get("developer_data"))
        public_interest_stats = from_union([PublicInterestStats.from_dict, from_none], obj.get("public_interest_stats"))
        status_updates = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("status_updates"))
        last_updated = from_union([from_datetime, from_none], obj.get("last_updated"))
        tickers = from_union([lambda x: from_list(Ticker.from_dict, x), from_none], obj.get("tickers"))
        return Coin(asset_platform_id, hashing_algorithm, public_notice, genesis_date, sentiment_votes_up_percentage,
                    sentiment_votes_down_percentage, id, symbol, name, platforms, block_time_in_minutes, categories,
                    additional_notices, description, links, image, country_origin, market_cap_rank, coingecko_rank,
                    coingecko_score, developer_score, community_score, liquidity_score, public_interest_score,
                    community_data, developer_data, public_interest_stats, status_updates, last_updated, tickers)

    def to_dict(self) -> dict:
        result: dict = {"asset_platform_id": from_none(self.asset_platform_id),
                        "hashing_algorithm": from_none(self.hashing_algorithm),
                        "public_notice": from_none(self.public_notice), "genesis_date": from_none(self.genesis_date),
                        "sentiment_votes_up_percentage": from_none(self.sentiment_votes_up_percentage),
                        "sentiment_votes_down_percentage": from_none(self.sentiment_votes_down_percentage),
                        "id": from_union([from_str, from_none], self.id),
                        "symbol": from_union([from_str, from_none], self.symbol),
                        "name": from_union([from_str, from_none], self.name),
                        "platforms": from_union([lambda x: to_class(Platforms, x), from_none], self.platforms),
                        "block_time_in_minutes": from_union([from_int, from_none], self.block_time_in_minutes),
                        "categories": from_union([lambda x: from_list(from_str, x), from_none], self.categories),
                        "additional_notices": from_union([lambda x: from_list(lambda x: x, x), from_none],
                                                         self.additional_notices),
                        "description": from_union([lambda x: to_class(Description, x), from_none], self.description),
                        "links": from_union([lambda x: to_class(Links, x), from_none], self.links),
                        "image": from_union([lambda x: to_class(Image, x), from_none], self.image),
                        "country_origin": from_union([from_str, from_none], self.country_origin),
                        "market_cap_rank": from_union([from_int, from_none], self.market_cap_rank),
                        "coingecko_rank": from_union([from_int, from_none], self.coingecko_rank),
                        "coingecko_score": from_union([to_float, from_none], self.coingecko_score),
                        "developer_score": from_union([to_float, from_none], self.developer_score),
                        "community_score": from_union([to_float, from_none], self.community_score),
                        "liquidity_score": from_union([to_float, from_none], self.liquidity_score),
                        "public_interest_score": from_union([from_int, from_none], self.public_interest_score),
                        "community_data": from_union([lambda x: to_class(CommunityData, x), from_none],
                                                     self.community_data),
                        "developer_data": from_union([lambda x: to_class(DeveloperData, x), from_none],
                                                     self.developer_data),
                        "public_interest_stats": from_union([lambda x: to_class(PublicInterestStats, x), from_none],
                                                            self.public_interest_stats),
                        "status_updates": from_union([lambda x: from_list(lambda x: x, x), from_none],
                                                     self.status_updates),
                        "last_updated": from_union([lambda x: x.isoformat(), from_none], self.last_updated),
                        "tickers": from_union([lambda x: from_list(lambda x: to_class(Ticker, x), x), from_none],
                                              self.tickers)}
        return result


def coin_from_dict(s: Any) -> Coin:
    return Coin.from_dict(s)


def coin_to_dict(x: Coin) -> Any:
    return to_class(Coin, x)
