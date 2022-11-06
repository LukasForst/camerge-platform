import datetime
import json
import logging
import os.path
from typing import Optional, Dict

import dacite
from dacite import from_dict

from common.model import CalendarConfiguration
from common.storage import Storage

logger = logging.getLogger(__name__)


class ReadOnlyStaticFileStorage(Storage):
    """
    Implementation of Storage that supports only reading from static file.
    """

    def __init__(self,
                 file_path: str
                 ):
        if not os.path.exists(file_path):
            raise Exception(f'Path {file_path} does not exist! Can not read.')

        self.__file_path = file_path

    def get(self, key: str) -> Optional[CalendarConfiguration]:
        return self.__load_data().get(key, None)

    def __load_data(self) -> Dict[str, CalendarConfiguration]:
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                return {key: from_dict(data_class=CalendarConfiguration, data=calendar,
                                       config=dacite.Config(type_hooks={datetime.date: datetime.date.fromisoformat}),
                                       )
                        for key, calendar in data.items()}
        except Exception as ex:
            logger.exception(ex)
            return dict()

    def store(self, calendar: CalendarConfiguration, key: Optional[str] = None) -> str:
        raise Exception('This is read only implementation of Storage!')
