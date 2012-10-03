import tornado.web
from tornado import gen
import elephunk.databases.helpers

class DatabasesHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @gen.engine
    def get(self):
        rows = yield gen.Task(self.application.db.select_all, "SELECT * FROM pg_stat_database")
        self.render("databases/index.html", databases=rows, percent=elephunk.databases.helpers.percent)
