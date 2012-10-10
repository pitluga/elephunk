from http_test_case import HTTPTestCase

class BloatServerHandlerTest(HTTPTestCase):

    def test_get(self):
        response = self.get("/bloat")
        self.assertEquals(200, response.code)
