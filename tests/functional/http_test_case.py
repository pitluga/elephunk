from os.path import realpath, join
from urllib import urlencode
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.httputil import HTTPHeaders
from tornado.ioloop import IOLoop
from tornado.testing import AsyncHTTPTestCase

import elephunk.application

class HTTPTestCase(AsyncHTTPTestCase):

    def get_new_ioloop(self):
        return IOLoop.instance()

    def get_app(self):
        config = realpath(join(realpath(__file__), '..', '..', '..', 'development.yml'))
        return elephunk.application.create(self.get_http_port(), False, config)

    def get(self, path, headers={}):
        client = AsyncHTTPClient(IOLoop.instance())
        request = HTTPRequest(self.get_url(path), headers=HTTPHeaders(headers))
        client.fetch(request, self.stop)
        return self.wait()

    def post(self, path, body, headers={}):
        client = AsyncHTTPClient(IOLoop.instance())
        request = HTTPRequest(self.get_url(path), method="POST", body=urlencode(body), headers=HTTPHeaders(headers), follow_redirects=False)
        client.fetch(request, self.stop)
        return self.wait()

