from unittest import TestCase
from tornado.escape import json_decode
from elephunk.handlers import IndexesDatabaseHandler
from elephunk.database import Row

class IndexesDatabaseHandlerTest(TestCase):

    def test_build_index_json(self):
        tables = [
            Row(relid=1, schemaname='public', relname='table1', seq_scan=20, seq_tup_read=200),
            Row(relid=2, schemaname='public', relname='table2', seq_scan=10, seq_tup_read=100)
        ]
        indexes = [
            Row(relid=1, schemaname='public', relname='table1', indexrelname='index1', idx_scan=100, idx_tup_read=700, idx_tup_fetch=80, indisunique=True),
            Row(relid=1, schemaname='public', relname='table1', indexrelname='index2', idx_scan=50, idx_tup_read=70, idx_tup_fetch=8, indisunique=False),
            Row(relid=2, schemaname='public', relname='table2', indexrelname='index3', idx_scan=100, idx_tup_read=700, idx_tup_fetch=80, indisunique=True)
        ]

        json = json_decode(IndexesDatabaseHandler.build_json('database', tables, indexes))
        self.assertEquals('database', json['name'])
        self.assertEquals(['public.table1', 'public.table2'], [c['name'] for c in json['children']])

    def test_map_table(self):
        table = Row(relid=1, schemaname='public', relname='table1', seq_scan=20, seq_tup_read=200)
        mapped_table = IndexesDatabaseHandler.map_table(table, {})

        self.assertEquals('public.table1', mapped_table['name'])
        self.assertEquals('public.table1.unindexed', mapped_table['children'][0]['name'])
        self.assertEquals(20, mapped_table['children'][0]['scans'])
        self.assertEquals(200, mapped_table['children'][0]['tuples'])
        self.assertEquals(False, mapped_table['children'][0]['isIndex'])

    def test_map_index(self):
        index = Row(relid=1, schemaname='public', relname='table1', indexrelname='index1', idx_scan=100, idx_tup_read=700, idx_tup_fetch=80, indisunique=True)
        mapped_index = IndexesDatabaseHandler.map_index(index)
        self.assertEquals('public.table1.index1', mapped_index['name'])
        self.assertEquals(100, mapped_index['scans'])
        self.assertEquals(780, mapped_index['tuples'])
        self.assertEquals(True, mapped_index['isUnique'])



