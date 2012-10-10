from activity_handler import ActivityHandler
from bloat_server_handler import BloatServerHandler
from buffer_cache_database_handler import BufferCacheDatabaseHandler
from buffer_cache_server_handler import BufferCacheServerHandler
from indexes_server_handler import IndexesServerHandler
from indexes_database_handler import IndexesDatabaseHandler
from indexes_table_handler import IndexesTableHandler
from root_handler import RootHandler
from select_server_handler import SelectServerHandler
from server_stats_handler import ServerStatsHandler

def handlers():
    return [(r"/", RootHandler),
            (r"/select-server", SelectServerHandler),
            (r"/activity", ActivityHandler),
            (r"/bloat", BloatServerHandler),
            (r"/buffer-cache", BufferCacheServerHandler),
            (r"/buffer-cache/([0-9]+)", BufferCacheDatabaseHandler),
            (r"/indexes", IndexesServerHandler),
            (r"/indexes/([0-9]+)", IndexesDatabaseHandler),
            (r"/indexes/([0-9]+)/([0-9]+)", IndexesTableHandler)]
