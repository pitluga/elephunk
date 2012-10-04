import yaml
import tornado.web

import elephunk
import elephunk.activity
import elephunk.stats
import elephunk.database

def create(port, debug, config_file):
    with open(config_file, 'r') as f:
        config = yaml.load(f.read())

    handlers = elephunk.handlers()
    handlers += elephunk.activity.handlers()
    handlers += elephunk.stats.handlers()

    application = tornado.web.Application(handlers, debug=debug, template_path="templates", static_path="static")
    application.db = elephunk.database.DatabaseClients(config['servers'])
    application.listen(port)

    return application
