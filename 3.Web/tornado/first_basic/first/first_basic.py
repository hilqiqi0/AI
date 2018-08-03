from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('Hello Tornado')

    def post(self, *args, **kwargs):
        pass


app = Application(handlers=[('/', IndexHandler)])
server = HTTPServer(app)
server.listen(8888)
IOLoop.current().start()
