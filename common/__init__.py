import logging
from typing import Optional, Tuple

from camerge import merge_calendars

from common.model import CalendarConfiguration
from common.storage import Storage
from common.storage.in_memory import InMemoryStorage

logger = logging.getLogger(__name__)


class Camerge:
    def __init__(self,
                 store: Optional[Storage] = None
                 ):
        self.__storage = store if store else InMemoryStorage()

    def get_for_key(self, key: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Returns [serialized calendar, error].
        """
        logger.debug(f'Calendar request for key "{key}".')
        try:
            maybe_configuration = self.__storage.get(key)
            logger.debug(f'Configuration for key "{key}" was {"found" if maybe_configuration else "not found"}.')

            if maybe_configuration:
                return self.__get_calendar_for_configuration(maybe_configuration), None
            else:
                return None, f'Key "{key}" does not exist!'
        except Exception as ex:
            logger.exception(ex)
            return None, f'{ex}'

    @staticmethod
    def __get_calendar_for_configuration(conf: CalendarConfiguration) -> str:
        ical = merge_calendars(
            calendar_name=conf.calendar_name,
            calendar_domain=conf.calendar_domain,
            calendar_urls=[(c.url, c.anonymize) for c in conf.calendar_urls],
            known_emails=conf.known_emails,
            skip_events_before=conf.skip_events_before
        )
        return ical
