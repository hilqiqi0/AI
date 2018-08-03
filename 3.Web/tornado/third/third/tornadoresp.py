import json

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_config_file
from tornado.web import Application, RequestHandler


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')

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

    def set_default_headers(self):
        #让继承者自定义响应头中的内容
        print('set_default_headers方法被调用')

    def initialize(self):
        # 让继承者在执行get/post方法之前传入参数
        # 或者执行一些初始化操作
        print('initialize方法被调用了')

    def on_finish(self):
        #执行get/post方法执行完毕后，释放资源
        print('on_finish方法被调用了')

    def get(self, *args, **kwargs):
        print('get方法被调用了')
        #以JSON字符串作为响应内容
        #JSON字符串的格式
        #｛"key":"value","key2":"value2"｝
        resp = {'key1':'value1',
                'key2':'value2'}

        #self.write(resp)
        #Content - Type: application / json;
        #charset = UTF - 8
        self.set_header('Content-Type',
                        'application/json;charset=UTF-8')
        json_str = json.dumps(resp)
        self.write(json_str)
    def post(self, *args, **kwargs):
        pass


define('duankou',type=int,default=8888)
parse_config_file('../config/config')
app = Application(handlers=[('/',IndexHandler),
                            ('/login',LoginHandler),
                            ('/blog',BlogHandler)],
                  template_path='mytemplate')
server = HTTPServer(app)
server.listen(options.duankou)
IOLoop.current().start()