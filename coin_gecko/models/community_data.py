from dataclasses import dataclass
from typing import Optional, Any

from coin_gecko.util import from_none, from_union, from_int


@dataclass
class CommunityData:
    facebook_likes: None
    twitter_followers: Optional[int] = None
    reddit_average_posts_48_h: Optional[int] = None
    reddit_average_comments_48_h: Optional[int] = None
    reddit_subscribers: Optional[int] = None
    reddit_accounts_active_48_h: Optional[int] = None
    telegram_channel_user_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CommunityData':
        assert isinstance(obj, dict)
        facebook_likes = from_none(obj.get("facebook_likes"))
        twitter_followers = from_union([from_int, from_none], obj.get("twitter_followers"))
        reddit_average_posts_48_h = from_union([from_int, from_none], obj.get("reddit_average_posts_48h"))
        reddit_average_comments_48_h = from_union([from_int, from_none], obj.get("reddit_average_comments_48h"))
        reddit_subscribers = from_union([from_int, from_none], obj.get("reddit_subscribers"))
        reddit_accounts_active_48_h = from_union([from_int, from_none], obj.get("reddit_accounts_active_48h"))
        telegram_channel_user_count = from_union([from_int, from_none], obj.get("telegram_channel_user_count"))
        return CommunityData(facebook_likes,
                             twitter_followers,
                             reddit_average_posts_48_h,
                             reddit_average_comments_48_h,
                             reddit_subscribers,
                             reddit_accounts_active_48_h,
                             telegram_channel_user_count
                             )

    def to_dict(self) -> dict:
        result: dict = {"facebook_likes": from_none(self.facebook_likes),
                        "twitter_followers": from_union([from_int, from_none], self.twitter_followers),
                        "reddit_average_posts_48h": from_union([from_int, from_none], self.reddit_average_posts_48_h),
                        "reddit_average_comments_48h": from_union([from_int, from_none],
                                                                  self.reddit_average_comments_48_h),
                        "reddit_subscribers": from_union([from_int, from_none], self.reddit_subscribers),
                        "reddit_accounts_active_48h": from_union([from_int, from_none],
                                                                 self.reddit_accounts_active_48_h),
                        "telegram_channel_user_count": from_union([from_int, from_none],
                                                                  self.telegram_channel_user_count)}
        return result
