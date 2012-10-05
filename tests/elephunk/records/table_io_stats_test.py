from unittest import TestCase
from elephunk.records.table_io_stats import TableIOStats

class TableIOStatsTest(TestCase):

    def test_heap_blks_accessed_sums(self):
        stats = TableIOStats(heap_blks_read=10, heap_blks_hit=1)
        self.assertEquals(11, stats.heap_blks_accessed)

    def test_heap_blks_accessed_treats_none_as_zero(self):
        self.assertEquals(0, TableIOStats(heap_blks_read=None, heap_blks_hit=None).heap_blks_accessed)
        self.assertEquals(1, TableIOStats(heap_blks_read=1, heap_blks_hit=None).heap_blks_accessed)
        self.assertEquals(10, TableIOStats(heap_blks_read=None, heap_blks_hit=10).heap_blks_accessed)

    def test_idx_blks_accessed_sums(self):
        stats = TableIOStats(idx_blks_read=10, idx_blks_hit=1)
        self.assertEquals(11, stats.idx_blks_accessed)

    def test_idx_blks_accessed_treats_none_as_zero(self):
        self.assertEquals(0, TableIOStats(idx_blks_read=None, idx_blks_hit=None).idx_blks_accessed)
        self.assertEquals(1, TableIOStats(idx_blks_read=1, idx_blks_hit=None).idx_blks_accessed)
        self.assertEquals(10, TableIOStats(idx_blks_read=None, idx_blks_hit=10).idx_blks_accessed)

    def test_toast_blks_accessed_sums(self):
        stats = TableIOStats(toast_blks_read=10, toast_blks_hit=1)
        self.assertEquals(11, stats.toast_blks_accessed)

    def test_toast_blks_accessed_treats_none_as_zero(self):
        self.assertEquals(0, TableIOStats(toast_blks_read=None, toast_blks_hit=None).toast_blks_accessed)
        self.assertEquals(1, TableIOStats(toast_blks_read=1, toast_blks_hit=None).toast_blks_accessed)
        self.assertEquals(10, TableIOStats(toast_blks_read=None, toast_blks_hit=10).toast_blks_accessed)

    def test_tidx_blks_accessed_sums(self):
        stats = TableIOStats(tidx_blks_read=10, tidx_blks_hit=1)
        self.assertEquals(11, stats.tidx_blks_accessed)

    def test_tidx_blks_accessed_treats_none_as_zero(self):
        self.assertEquals(0, TableIOStats(tidx_blks_read=None, tidx_blks_hit=None).tidx_blks_accessed)
        self.assertEquals(1, TableIOStats(tidx_blks_read=1, tidx_blks_hit=None).tidx_blks_accessed)
        self.assertEquals(10, TableIOStats(tidx_blks_read=None, tidx_blks_hit=10).tidx_blks_accessed)
