from typing import Optional, Tuple

from common.model import CalendarConfiguration


class Storage:

    def get(self, key: str) -> Optional[CalendarConfiguration]:
        """
        Returns calendar configuration stored under given key or None when there's no calendar.
        """
        pass

    def store(self, calendar: CalendarConfiguration, key: Optional[str] = None) -> str:
        """
        Stores calendar given calendar configuration. If key is not given, new is generated.
        Returns key of the calendar
        """
        pass

    def get_or_store(self, key: str, calendar: CalendarConfiguration) -> Tuple[str, CalendarConfiguration]:
        maybe_calendar = self.get(key)
        if not maybe_calendar:
            key = self.store(calendar=calendar, key=key)
        return key, maybe_calendar if maybe_calendar else calendar
