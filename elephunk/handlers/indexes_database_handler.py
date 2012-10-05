from tornado import gen
from tornado.web import asynchronous
from base_handler import BaseHandler

class IndexesDatabaseHandler(BaseHandler):

    @asynchronous
    @gen.engine
    def get(self, datid):
        database_name = yield gen.Task(self.client_for('postgres').select_scalar, "SELECT datname FROM pg_stat_database WHERE datid = %s", (datid,))
        tables = yield gen.Task(self.client_for(database_name).select_all, "SELECT * FROM pg_stat_user_tables")
        self.render('indexes/database.html', database_name=database_name, tables=tables)

