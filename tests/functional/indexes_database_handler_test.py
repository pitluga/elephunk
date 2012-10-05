from http_test_case import HTTPTestCase

class IndexesDatabaseHandlerTest(HTTPTestCase):

    def test_get(self):
        response = self.get("/indexes/1")
        self.assertEquals(200, response.code)


