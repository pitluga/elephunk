from http_test_case import HTTPTestCase

class IndexesServerHandlerTest(HTTPTestCase):

    def test_get(self):
        response = self.get("/indexes")
        self.assertEquals(200, response.code)

