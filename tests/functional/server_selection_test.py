from http_test_case import HTTPTestCase
from pyquery import PyQuery

class ServerSelectionTest(HTTPTestCase):

    def test_defaults_to_first_server_in_list(self):
        response = self.get('/')
        html = PyQuery(response.body)
        self.assertIn("localhost", html('#selected-server').html())

    def test_server_stored_in_cookie(self):
        response = self.get('/', {'Cookie': "selected-server=localhost"})
        html = PyQuery(response.body)
        self.assertIn("localhost", html('#selected-server').html())

    def test_posting_to_select_server_sets_cookie(self):
        response = self.post('/select-server', dict(server='localhost'), headers={'Referer': "http://localhost"})
        self.assertIn('selected-server=localhost', response.headers['Set-Cookie'])
        self.assertEquals(302, response.code)
        self.assertEquals('http://localhost', response.headers['Location'])
