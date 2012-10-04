import tornado.web
from tornado import gen
from elephunk.activity.activity_presenter import ActivityPresenter

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @gen.engine
    def get(self):
        rows = yield gen.Task(self.application.db.client('localhost','postgres').select_all, "SELECT * FROM pg_stat_activity")
        self.render("activity/index.html", presenter=ActivityPresenter(rows))
