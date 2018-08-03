from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler


define('duankou',type=int,default=8888)
parse_config_file('../config/config')


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('<a href=/java>Try try Java</a><br>')
        self.write('<a href=/python>Try try Python</a>')
    def post(self, *args, **kwargs):
        pass

class JavaHandler(RequestHandler):
    def get(self, p1=None,p2=None,*args, **kwargs):
        # get() missing 1 required positional argument: 'p2'
        # Can't convert 'NoneType' object to str implicitly(隐式)
        self.write('Hello Java<br>')
        if p1:
            self.write('今天是：'+p1+'<br>')
        else:
            self.write('day1,day2,day3,day4...')
        if p2:
            self.write('课程是：'+p2)
    def post(self, *args, **kwargs):
        pass

class PythonHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('Hello Python')
        #获取用户的请求参数
        #400 Missing argument subject
        d = self.get_query_argument('day',None)
        s = self.get_query_argument('subject',None)
        ds = self.get_query_arguments('day')
        ss = self.get_query_arguments('subject')
        print(d,s)
        print(ds,ss)
    def post(self, *args, **kwargs):
        self.write('Hello Python POST')
        d = self.get_body_argument('day',None)
        s = self.get_body_argument('subject',None)
        print(d,s)
        ds = self.get_body_arguments('day')
        ss = self.get_body_arguments('subject')
        print(ds,ss)

        #get_argument(s)=get_query_argument(s) + get_body_argment(s)
        arg_d = self.get_argument('day',None)
        arg_ds = self.get_arguments('day')
        print(arg_d)
        print(arg_ds)

app = Application(handlers=[('/',IndexHandler),
                            ('/java',JavaHandler),
                            ('/java/(day[0-9]+)',JavaHandler),
                            ('/java/(day[0-9]+)/([a-z0-9]+)',JavaHandler),


                            ('/python',PythonHandler)])
server = HTTPServer(app)
server.listen(options.duankou)
IOLoop.current().start()
