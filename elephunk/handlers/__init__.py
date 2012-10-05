from activity_handler import ActivityHandler
from database_io_stats_handler import DatabaseIOStatsHandler
from root_handler import RootHandler
from select_server_handler import SelectServerHandler
from server_stats_handler import ServerStatsHandler

def handlers():
    return [(r"/", RootHandler),
            (r"/select-server", SelectServerHandler),
            (r"/activity", ActivityHandler),
            (r"/stats", ServerStatsHandler),
            (r"/stats/([0-9]+)", DatabaseIOStatsHandler)]
