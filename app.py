import logging
import tornado.ioloop
import elephunk.application

application = elephunk.application.create()
logging.basicConfig()

if __name__ == "__main__":
    application.listen(8888)
    logging.info("Starting application on port 8888")
    tornado.ioloop.IOLoop.instance().start()
