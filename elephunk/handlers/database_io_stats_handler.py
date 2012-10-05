from tornado import gen
from tornado.web import asynchronous
from base_handler import BaseHandler
from elephunk.records.table_io_stats import TableIOStats

class DatabaseIOStatsHandler(BaseHandler):

    @asynchronous
    @gen.engine
    def get(self, datid):
        print datid
        database_name = yield gen.Task(self.client_for('postgres').select_scalar, "SELECT datname FROM pg_stat_database WHERE datid = %s", (datid,))
        tables = yield gen.Task(self.client_for(database_name).select_all, "SELECT * FROM pg_statio_user_tables", record=TableIOStats)
        self.render('stats/database.html', database_name=database_name, tables=tables)
