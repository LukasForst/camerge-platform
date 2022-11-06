from typing import Optional, Dict, Callable
from uuid import uuid4

from common.model import CalendarConfiguration
from common.storage import Storage


class InMemoryStorage(Storage):
    """
    Implementation of Storage that stores data in memory.
    """

    def __init__(self,
                 storage: Optional[Dict[str, CalendarConfiguration]] = None,
                 key_gen: Optional[Callable[[], str]] = None
                 ):
        self.__map = storage if storage else dict()
        self.__key_gen = key_gen if key_gen else lambda: str(uuid4())

    def get(self, key: str) -> Optional[CalendarConfiguration]:
        return self.__map.get(key, None)

    def store(self, calendar: CalendarConfiguration, key: Optional[str] = None) -> str:
        key = key if key else self.__key_gen()
        self.__map[key] = calendar
        return key
