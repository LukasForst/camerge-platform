from unittest import TestCase

from common import Camerge
from common.storage.static_file import ReadOnlyStaticFileStorage
from tests import data


class TestCamerge(TestCase):

    def test_real_ics_parsing(self):
        camerge = Camerge(store=ReadOnlyStaticFileStorage(data('test_real_ics_calendar.json')))
        ics, error = camerge.get_for_key('c1')
        self.assertIsNotNone(ics)
        self.assertIsNone(error)

        self.assertIn('STATUS:TENTATIVE', ics)
        self.assertIn('SUMMARY:busy', ics)
        self.assertIn('UID:4fdade89dd887bf4d663baa7bfb8f373@real.com', ics)
