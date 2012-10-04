from http_test_case import HTTPTestCase

class MainHanlderTest(HTTPTestCase):

    def test_get(self):
        response = self.get("/activity")
        self.assertIn("activity", response.body)
