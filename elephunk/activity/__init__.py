import main_handler

def handlers():
    return [(r"/activity", main_handler.MainHandler)]
