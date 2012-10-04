import tornado.web

class SelectServerHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_cookie("selected-server", self.get_argument("server"))
        self.redirect(self.request.headers['Referer'])

