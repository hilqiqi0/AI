import json

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_config_file
from tornado.web import Application, RequestHandler, UIModule


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):

        r = ''
        msg = self.get_query_argument('msg',None)
        if msg:
            r='用户名或密码错误'
        self.render('login.html',result=r)

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

        self.render('blog.html')

    def post(self, *args, **kwargs):
        pass

    def my_f(self,a,b):
        return a+b

class LoginModule(UIModule):
    def render(self, *args, **kwargs):
        #NameError: name 'result' is not defined
        print(self.request)
        print(self.request.uri)#uri = 路径＋参数
        print(self.request.path)#uri中的路径
        print(self.request.query)#uri中的参数

        r = ''
        if self.request.query:
            r = '用户名或密码错误'

        return self.render_string('mymodule/login_module.html',result=r)

class BlogModule(UIModule):
    def render(self, *args, **kwargs):
        return self.render_string('mymodule/blog_module.html',blogs=[{
                        'author':'大旭旭',
                        'avatar':'a.jpg',
                        'title':'办证',
                        'content':'联系电话13843819438',
                        'tags':'IT 教育',
                        'count':8
                    },{
                        'author': '小超超',
                        'avatar':None,
                        'title': '晚上吃啥好?',
                        'content': '漫漫长夜，订个外卖可好?',
                        'tags': '情感 星座',
                        'count': 0
                    },{
                        'author': 'Harry',
                        'avatar':'a.jpg',
                        'title': '英格兰必胜',
                        'content': '预测比分3:0!',
                        'tags': '体育 星座',
                        'count': 3
                    },{
                        'author': '闵大神',
                        'avatar':None,
                        'title': '人工智能我最懂',
                        'content': '我可以成功预测昨天的天气情况！',
                        'tags': '教育 科技',
                        'count': 0
                    }])

class RegistHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('regist.html')
    def post(self, *args, **kwargs):
        pass

define('duankou',type=int,default=8888)
parse_config_file('../config/config')
app = Application(handlers=[('/',IndexHandler),
                            ('/login',LoginHandler),
                            ('/blog',BlogHandler),
                            ('/regist',RegistHandler)],
                  template_path='mytemplate',
                  static_path='mystatics',
                  ui_modules={'loginmodule':LoginModule,
                              'blogmodule':BlogModule})
server = HTTPServer(app)
server.listen(options.duankou)
IOLoop.current().start()