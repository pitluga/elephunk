from tornado import gen
from tornado.web import asynchronous
from base_handler import BaseHandler

class IndexesServerHandler(BaseHandler):

    @asynchronous
    @gen.engine
    def get(self):
        rows = yield gen.Task(self.client_for('postgres').select_all, "SELECT * FROM pg_stat_database")
        self.render("indexes/server.html", databases=rows)
