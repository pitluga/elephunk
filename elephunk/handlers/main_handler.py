from tornado import gen
from tornado.web import asynchronous
from base_handler import BaseHandler
from elephunk.activity.activity_presenter import ActivityPresenter

class MainHandler(BaseHandler):
    @asynchronous
    @gen.engine
    def get(self):
        rows = yield gen.Task(self.client_for('postgres').select_all, "SELECT * FROM pg_stat_activity")
        self.render("activity/index.html", presenter=ActivityPresenter(rows))
