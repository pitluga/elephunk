from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
from tornado.testing import AsyncHTTPTestCase

import elephunk.application

class HTTPTestCase(AsyncHTTPTestCase):

    def get_new_ioloop(self):
        return IOLoop.instance()

    def get_app(self):
        return elephunk.application.create()

    def get(self, path):
        client = AsyncHTTPClient(IOLoop.instance())
        client.fetch(self.get_url(path), self.stop)
        return self.wait()
