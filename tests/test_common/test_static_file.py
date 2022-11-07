import datetime
from unittest import TestCase

from common.storage.static_file import ReadOnlyStaticFileStorage
from tests import data


class TestReadOnlyStaticFileStorage(TestCase):

    def test_static_read_can_parse_data(self):
        storage = ReadOnlyStaticFileStorage(data('test_calendar_conf.json'))
        calendar = storage.get('firstCalendar')
        self.assertIsNotNone(calendar)
        self.assertTrue(isinstance(calendar.skip_events_before, datetime.date))