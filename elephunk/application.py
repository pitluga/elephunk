import yaml
import tornado.web

import elephunk.handlers
import elephunk.database
import elephunk.uimodules
import elephunk.ui_methods

def create(port, debug, config_file):
    with open(config_file, 'r') as f:
        config = yaml.load(f.read())

    application = tornado.web.Application(
        elephunk.handlers.handlers(),
        debug=debug,
        template_path="templates",
        static_path="static",
        ui_modules=elephunk.uimodules,
        ui_methods=elephunk.ui_methods
    )
    application.db = elephunk.database.DatabaseClients(config['servers'])
    application.listen(port)

    return application
