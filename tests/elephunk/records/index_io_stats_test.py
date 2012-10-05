from unittest import TestCase
from elephunk.records.index_io_stats import IndexIOStats

class IndexIOStatsTest(TestCase):

    def test_idx_blks_accessed_sums(self):
        stats = IndexIOStats(idx_blks_read=10, idx_blks_hit=1)
        self.assertEquals(11, stats.idx_blks_accessed)

    def test_idx_blks_accessed_treats_none_as_zero(self):
        self.assertEquals(0, IndexIOStats(idx_blks_read=None, idx_blks_hit=None).idx_blks_accessed)
        self.assertEquals(1, IndexIOStats(idx_blks_read=1, idx_blks_hit=None).idx_blks_accessed)
        self.assertEquals(10, IndexIOStats(idx_blks_read=None, idx_blks_hit=10).idx_blks_accessed)
