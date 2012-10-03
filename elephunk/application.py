import tornado.web
import momoko

import elephunk
import elephunk.activity
import elephunk.stats
import elephunk.database

def create(debug=False):
    handlers = elephunk.handlers()
    handlers += elephunk.activity.handlers()
    handlers += elephunk.stats.handlers()

    application = tornado.web.Application(handlers, debug=debug, template_path="templates", static_path="static")
    application.db = elephunk.database.Database(momoko.AsyncClient({
        'host': 'localhost',
        'port': 5432,
        'database': 'postgres',
    }))

    return application
