from unittest import TestCase
from elephunk.records.sequence_io_stats import SequenceIOStats

class SequenceIOStatsTest(TestCase):

    def test_blks_accessed_sums(self):
        stats = SequenceIOStats(blks_read=10, blks_hit=1)
        self.assertEquals(11, stats.blks_accessed)

    def test_blks_accessed_treats_none_as_zero(self):
        self.assertEquals(0, SequenceIOStats(blks_read=None, blks_hit=None).blks_accessed)
        self.assertEquals(1, SequenceIOStats(blks_read=1, blks_hit=None).blks_accessed)
        self.assertEquals(10, SequenceIOStats(blks_read=None, blks_hit=10).blks_accessed)

