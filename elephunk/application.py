import tornado.web
import momoko

import elephunk
import elephunk.activity
import elephunk.databases
import elephunk.database

def create():
    handlers = elephunk.handlers()
    handlers += elephunk.activity.handlers()
    handlers += elephunk.databases.handlers()

    application = tornado.web.Application(handlers, debug=True, template_path="templates", static_path="static")
    application.db = elephunk.database.Database(momoko.AsyncClient({
        'host': 'localhost',
        'port': 5432,
        'database': 'postgres',
    }))

    return application
