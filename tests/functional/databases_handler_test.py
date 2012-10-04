from http_test_case import HTTPTestCase

class MainHanlderTest(HTTPTestCase):

    def test_get(self):
        response = self.get("/stats")
        self.assertEquals(200, response.code)

