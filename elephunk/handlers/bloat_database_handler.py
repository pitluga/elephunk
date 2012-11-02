from tornado import gen
from tornado.web import asynchronous
from tornado.escape import json_encode
from base_handler import BaseHandler
from elephunk.records import Bloat

class BloatDatabaseHandler(BaseHandler):

    @asynchronous
    @gen.engine
    def get(self, datid):
        database_name = yield gen.Task(self.client_for('postgres').select_scalar, "SELECT datname FROM pg_stat_database WHERE datid = %s", (datid,))
        rows = yield gen.Task(self.client_for(database_name).select_all, Bloat.sql(), record=Bloat)
        self.render("bloat/database.html", datid=datid, database_name=database_name, bloat_data=self.build_json(database_name, rows))

    @staticmethod
    def map_index(index):
        return dict(name=index.iname, children=[dict(name=index.iname, isBloat=False, value=int(index.iusedbytes)), dict(name="%s bloat" % index.iname, isBloat=True, value=int(index.ibloat))])

    @staticmethod
    def map_table(table, indexes):
        return dict(name=table.full_table_name, children=[dict(name="%s bloat" % table.full_table_name, isBloat=True, value=int(table.wastedbytes))] + indexes.get(table.table_id, []))

    @staticmethod
    def build_index(indexes, index):
        if index.table_id not in indexes:
            indexes[index.table_id] = [BloatDatabaseHandler.map_index(index)]
        else:
            indexes[index.table_id].append(BloatDatabaseHandler.map_index(index))

        return indexes

    @staticmethod
    def create_table_builder(indexes):
        def build_table(tables, table):
            if table.table_id not in tables:
                tables[table.table_id] = BloatDatabaseHandler.map_table(table, indexes)
            return tables

        return build_table

    def build_json(self, database_name, rows):
        indexes = reduce(BloatDatabaseHandler.build_index, rows, {})
        tables = reduce(BloatDatabaseHandler.create_table_builder(indexes), rows, {})
        return json_encode(dict(name=database_name, children=tables.values()))

