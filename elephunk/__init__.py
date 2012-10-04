from root_handler import RootHandler
from select_server_handler import SelectServerHandler

def handlers():
    return [(r"/", RootHandler),
            (r"/select-server", SelectServerHandler)]
