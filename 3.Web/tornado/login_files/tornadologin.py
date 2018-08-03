from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_config_file
from tornado.web import Application, RequestHandler


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):

        html='<form method=post action=/login enctype=multipart/form-data>' \
             '<span>用户名：</span>' \
             '<input type=text name=username><br>' \
             '<span>密码：</span>' \
             '<input type=password name=password><br>' \
             '<input type=file name=avatar><br>' \
             '<input type=file name=avatar><br>' \
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
            #如果用户真上传了文件
            #把上传的文件保存到服务器
            #self.request是RequestHandler
            #的一个属性，引用HttpServerReqeust对象
            #该对象中封装了与请求相关的所有内容
            print(self.request)
            #HttpServerRequest对象的files属性
            #引用着用户通过表单上传的文件
            #如果用户没有上传文件，files属性是空字典{}
            #如果上传了文件
            #{'avatar':[{
            # 'content_type':'image/jpeg',
            # 'body':二进制格式表示的图像的内容,
            # 'filename':上传者本地图像名称},
            # {},
            # {}....]}
            print(self.request.files)
            if self.request.files:
                avs = self.request.files['avatar']
                for a in avs:
                    body = a['body']
                    #上传的这一个个文件内容
                    #保存到服务器的硬盘上
                    writer = open('upload/%s'%a['filename'],
                                  'wb')
                    writer.write(body)
                    writer.close()

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