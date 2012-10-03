import root_handler

def handlers():
    return [(r"/", root_handler.RootHandler)]
