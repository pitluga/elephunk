import unittest
from elephunk.database import Row
from elephunk.activity.activity_presenter import ActivityPresenter

class ActivityPresenterTest(unittest.TestCase):

    def test_active_connections(self):
        presenter = ActivityPresenter([Row(current_query="<IDLE>"), Row(current_query="SELECT 1")])
        self.assertEquals(1, len(presenter.active_connections()))

    def test_connections(self):
        presenter = ActivityPresenter([Row(current_query="<IDLE>"), Row(current_query="SELECT 1")])
        self.assertEquals(2, len(presenter.connections()))

