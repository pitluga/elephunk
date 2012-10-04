from main_handler import MainHandler
from databases_handler import DatabasesHandler
from root_handler import RootHandler
from select_server_handler import SelectServerHandler

def handlers():
    return [(r"/", RootHandler),
            (r"/select-server", SelectServerHandler),
            (r"/activity", MainHandler),
            (r"/stats", DatabasesHandler)]
