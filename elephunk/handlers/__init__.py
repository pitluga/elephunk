from activity_handler import ActivityHandler
from buffer_cache_database_handler import BufferCacheDatabaseHandler
from buffer_cache_server_handler import BufferCacheServerHandler
from indexes_server_handler import IndexesServerHandler
from root_handler import RootHandler
from select_server_handler import SelectServerHandler
from server_stats_handler import ServerStatsHandler

def handlers():
    return [(r"/", RootHandler),
            (r"/select-server", SelectServerHandler),
            (r"/activity", ActivityHandler),
            (r"/buffer-cache", BufferCacheServerHandler),
            (r"/buffer-cache/([0-9]+)", BufferCacheDatabaseHandler),
            (r"/indexes", IndexesServerHandler)]
