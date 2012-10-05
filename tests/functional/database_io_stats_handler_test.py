from http_test_case import HTTPTestCase

class DatabaseIOStatsHandlerTest(HTTPTestCase):

    def test_get(self):
        response = self.get("/stats/1")
        self.assertEquals(200, response.code)


