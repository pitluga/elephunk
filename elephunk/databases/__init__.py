import databases_handler

def handlers():
    return [(r"/databases", databases_handler.DatabasesHandler)]

