import datetime
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CalendarUrl:
    url: str
    anonymize: bool


@dataclass
class CalendarConfiguration:
    calendar_name: str
    calendar_domain: str
    calendar_urls: List[CalendarUrl]
    known_emails: List[str]
    skip_events_before: Optional[datetime.date] = None
