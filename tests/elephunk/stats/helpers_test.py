import unittest
from elephunk.stats.helpers import *

class HelpersTest(unittest.TestCase):
    def test_percent(self):
        self.assertEquals("40%", percent(2,5))

    def test_percent_with_decimal(self):
        self.assertEquals("33.33%", percent(1,3))

    def test_infinity(self):
        self.assertEquals("infinity", percent(1,0))
