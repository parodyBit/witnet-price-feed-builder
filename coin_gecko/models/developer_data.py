from dataclasses import dataclass
from typing import Optional, Any, List, Dict, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser

from coin_gecko.models.code_tracking import CodeAdditionsDeletions4_Weeks
from coin_gecko.util import from_union, from_int, from_none, from_list, to_class


@dataclass
class DeveloperData:
    forks: Optional[int] = None
    stars: Optional[int] = None
    subscribers: Optional[int] = None
    total_issues: Optional[int] = None
    closed_issues: Optional[int] = None
    pull_requests_merged: Optional[int] = None
    pull_request_contributors: Optional[int] = None
    code_additions_deletions_4__weeks: Optional[CodeAdditionsDeletions4_Weeks] = None
    commit_count_4__weeks: Optional[int] = None
    last_4__weeks_commit_activity_series: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DeveloperData':
        assert isinstance(obj, dict)
        forks = from_union([from_int, from_none], obj.get("forks"))
        stars = from_union([from_int, from_none], obj.get("stars"))
        subscribers = from_union([from_int, from_none], obj.get("subscribers"))
        total_issues = from_union([from_int, from_none], obj.get("total_issues"))
        closed_issues = from_union([from_int, from_none], obj.get("closed_issues"))
        pull_requests_merged = from_union([from_int, from_none], obj.get("pull_requests_merged"))
        pull_request_contributors = from_union([from_int, from_none], obj.get("pull_request_contributors"))
        code_additions_deletions_4__weeks = from_union([CodeAdditionsDeletions4_Weeks.from_dict, from_none], obj.get("code_additions_deletions_4_weeks"))
        commit_count_4__weeks = from_union([from_int, from_none], obj.get("commit_count_4_weeks"))
        last_4__weeks_commit_activity_series = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("last_4_weeks_commit_activity_series"))
        return DeveloperData(forks,
                             stars,
                             subscribers,
                             total_issues,
                             closed_issues,
                             pull_requests_merged,
                             pull_request_contributors,
                             code_additions_deletions_4__weeks,
                             commit_count_4__weeks,
                             last_4__weeks_commit_activity_series
                             )

    def to_dict(self) -> dict:
        result: dict = {"forks": from_union([from_int, from_none], self.forks),
                        "stars": from_union([from_int, from_none], self.stars),
                        "subscribers": from_union([from_int, from_none], self.subscribers),
                        "total_issues": from_union([from_int, from_none], self.total_issues),
                        "closed_issues": from_union([from_int, from_none], self.closed_issues),
                        "pull_requests_merged": from_union([from_int, from_none], self.pull_requests_merged),
                        "pull_request_contributors": from_union([from_int, from_none], self.pull_request_contributors),
                        "code_additions_deletions_4_weeks": from_union(
                            [lambda x: to_class(CodeAdditionsDeletions4_Weeks, x), from_none],
                            self.code_additions_deletions_4__weeks),
                        "commit_count_4_weeks": from_union([from_int, from_none], self.commit_count_4__weeks),
                        "last_4_weeks_commit_activity_series": from_union(
                            [lambda x: from_list(lambda x: x, x), from_none],
                            self.last_4__weeks_commit_activity_series)}
        return result
