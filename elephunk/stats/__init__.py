import databases_handler

def handlers():
    return [(r"/stats", databases_handler.DatabasesHandler)]

