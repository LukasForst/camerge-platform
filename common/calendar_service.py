import datetime
from typing import Optional, Tuple

from camerge import merge_calendars


class CalendarService:

    def get_for_key(self, key: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Returns [serialized calendar, error].
        """
        try:
            return self.__get_default_calendar(), None
        except Exception as ex:
            return None, f'{ex}'

    def __get_default_calendar(self) -> str:
        ical = merge_calendars(
            calendar_name='My Availability',
            calendar_domain='my.calendar.example.com',
            calendar_urls=[],
            # take event availability from these email addresses, these should be your own
            # email addresses associated with the calendar accounts
            known_emails=[
                'me@example.com', 'otherme@example.com'
            ],
            # do not include events that are older than this
            skip_events_before=datetime.date(2021, 1, 1)
        )
        return ical
