from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_config_file
from tornado.web import Application, RequestHandler


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):

        html='<form method=post action=/login>' \
             '<span>用户名：</span>' \
             '<input type=text name=username><br>' \
             '<span>密码：</span>' \
             '<input type=password name=password><br>' \
             '<input type=submit value=登录>' \
             '&nbsp;&nbsp;' \
             '<input type=reset value=重置>' \
             '</form>'

        fail_html='<form method=post action=/login>' \
             '<span>用户名：</span>' \
             '<input type=text name=username><br>' \
             '<span>密码：</span>' \
             '<input type=password name=password><br>' \
             '<span style=color:red;>' \
                  '用户名或密码错误</span><br>' \
             '<input type=submit value=登录>' \
                  '&nbsp;&nbsp;' \
             '<input type=reset value=重置>' \
             '</form>'

        msg = \
            self.get_query_argument('msg',None)
        if msg:
            self.write(fail_html)
        else:
            self.write(html)
    def post(self, *args, **kwargs):
        pass

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        username = \
            self.get_body_argument('username',None)
        password = \
            self.get_body_argument('password',None)
        if username=='abc' and \
            password=='123':
            #跳转到blog页面
            self.redirect(
                '/blog?username='+username)
        else:
            #跳转回登录界面
            self.redirect('/?msg=fail')

class BlogHandler(RequestHandler):
    def get(self, *args, **kwargs):
        username = \
            self.get_query_argument(
                'username',None)
        if username:
            self.write('欢迎'+username+'使用')
        else:
            self.write('欢迎使用')
    def post(self, *args, **kwargs):
        pass


define('duankou',type=int,default=8888)
parse_config_file('../config/config')
app = Application(handlers=[('/',IndexHandler),
                            ('/login',LoginHandler),
                            ('/blog',BlogHandler)])
server = HTTPServer(app)
server.listen(options.duankou)
IOLoop.current().start()