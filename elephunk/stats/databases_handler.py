import tornado.web
from tornado import gen
from elephunk.stats.helpers import percent

class DatabasesHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @gen.engine
    def get(self):
        rows = yield gen.Task(self.application.db.select_all, "SELECT * FROM pg_stat_database")
        self.render("stats/index.html", databases=rows, percent=percent)
