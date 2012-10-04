from unittest import TestCase
from datetime import datetime
from elephunk.records.activity import Activity

class ActivityTest(TestCase):

    def test_formatted_xact_start_is_blank_when_none(self):
        self.assertEquals('', Activity(xact_start=None).formatted_xact_start)

    def test_formatted_xact_start_is_isoformatted(self):
        now = datetime.now()
        self.assertEquals(now.isoformat(), Activity(xact_start=now).formatted_xact_start)
