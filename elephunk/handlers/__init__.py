from activity_handler import ActivityHandler
from root_handler import RootHandler
from select_server_handler import SelectServerHandler
from server_stats_handler import ServerStatsHandler

def handlers():
    return [(r"/", RootHandler),
            (r"/select-server", SelectServerHandler),
            (r"/activity", ActivityHandler),
            (r"/stats", ServerStatsHandler)]
