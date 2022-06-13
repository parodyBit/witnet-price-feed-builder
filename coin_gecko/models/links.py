from dataclasses import dataclass
from typing import Optional, Any, List, Dict, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser

from coin_gecko.models.repo_url import ReposURL
from coin_gecko.util import from_none, from_union, from_list, from_str, to_class


@dataclass
class Links:
    bitcointalk_thread_identifier: None
    homepage: Optional[List[str]] = None
    blockchain_site: Optional[List[str]] = None
    official_forum_url: Optional[List[str]] = None
    chat_url: Optional[List[str]] = None
    announcement_url: Optional[List[str]] = None
    twitter_screen_name: Optional[str] = None
    facebook_username: Optional[str] = None
    telegram_channel_identifier: Optional[str] = None
    subreddit_url: Optional[str] = None
    repos_url: Optional[ReposURL] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Links':
        assert isinstance(obj, dict)
        bitcointalk_thread_identifier = from_none(obj.get("bitcointalk_thread_identifier"))
        homepage = from_union([lambda x: from_list(from_str, x), from_none], obj.get("homepage"))
        blockchain_site = from_union([lambda x: from_list(from_str, x), from_none], obj.get("blockchain_site"))
        official_forum_url = from_union([lambda x: from_list(from_str, x), from_none], obj.get("official_forum_url"))
        chat_url = from_union([lambda x: from_list(from_str, x), from_none], obj.get("chat_url"))
        announcement_url = from_union([lambda x: from_list(from_str, x), from_none], obj.get("announcement_url"))
        twitter_screen_name = from_union([from_str, from_none], obj.get("twitter_screen_name"))
        facebook_username = from_union([from_str, from_none], obj.get("facebook_username"))
        telegram_channel_identifier = from_union([from_str, from_none], obj.get("telegram_channel_identifier"))
        subreddit_url = from_union([from_str, from_none], obj.get("subreddit_url"))
        repos_url = from_union([ReposURL.from_dict, from_none], obj.get("repos_url"))
        return Links(bitcointalk_thread_identifier,
                     homepage,
                     blockchain_site,
                     official_forum_url,
                     chat_url,
                     announcement_url,
                     twitter_screen_name,
                     facebook_username,
                     telegram_channel_identifier,
                     subreddit_url,
                     repos_url
                     )

    def to_dict(self) -> dict:
        result: dict = {"bitcointalk_thread_identifier": from_none(self.bitcointalk_thread_identifier),
                        "homepage": from_union([lambda x: from_list(from_str, x), from_none], self.homepage),
                        "blockchain_site": from_union([lambda x: from_list(from_str, x), from_none],
                                                      self.blockchain_site),
                        "official_forum_url": from_union([lambda x: from_list(from_str, x), from_none],
                                                         self.official_forum_url),
                        "chat_url": from_union([lambda x: from_list(from_str, x), from_none], self.chat_url),
                        "announcement_url": from_union([lambda x: from_list(from_str, x), from_none],
                                                       self.announcement_url),
                        "twitter_screen_name": from_union([from_str, from_none], self.twitter_screen_name),
                        "facebook_username": from_union([from_str, from_none], self.facebook_username),
                        "telegram_channel_identifier": from_union([from_str, from_none],
                                                                  self.telegram_channel_identifier),
                        "subreddit_url": from_union([from_str, from_none], self.subreddit_url),
                        "repos_url": from_union([lambda x: to_class(ReposURL, x), from_none], self.repos_url)}
        return result
