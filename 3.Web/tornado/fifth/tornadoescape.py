from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('escape.html',result='')
    def post(self, *args, **kwargs):
        r = self.get_body_argument('result')
        self.render('escape.html',result=r)

define('duankou',type=int,default=8888)
parse_config_file('../config/config')
app = Application(handlers=[('/',IndexHandler)
                            ],
                  template_path='mytemplate',
                  autoescape=None
                  )
server = HTTPServer(app)
server.listen(options.duankou)
IOLoop.current().start()