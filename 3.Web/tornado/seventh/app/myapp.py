import time

from os import remove
from tornado.web import Application, RequestHandler, UIModule

from seventh.util.dbutil import DBUtil
from seventh.util.myutil import mymd5


class MyApplication(Application):
    def __init__(self,hs,tp,sp,um):

        super().__init__(handlers=hs,
                         template_path=tp,
                         static_path=sp,
                         ui_modules=um)

        self.dbutil = DBUtil()

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

        pwd = mymd5(password)

        # dbutil = self.application.dbutil

        if self.application.dbutil.isloginsuccess(username,pwd):
            self.redirect('/blog?username='+username)
        else:
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
        #cursor.fetchall()
        #(('作者','作者的头像'),(),())
        # [{},{},{}...]

        #dbutil = DBUtil()
        #UIModule无法直接找到Application对象
        #UIModule通过handler属性找到一个RequestHandler对象
        #然后再通过该RequestHandler对象找到Application对象
        blogs = self.handler.application.dbutil.getblogs()
        return self.render_string('mymodule/blog_module.html',blogs=blogs)

class RegistHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('regist.html')
    def post(self, *args, **kwargs):
        username = self.get_body_argument('username',None)
        password = self.get_body_argument('password',None)
        city = self.get_body_argument('city',None)

        if username and password and city:
            avatar = None
            if self.request.files:
                #{'avatar':[{'body','filename','content-type'},{}]}
                f = self.request.files['avatar'][0]
                print(f)
                body = f['body']
                fname = str(time.time()) + f['filename']
                writer = open('mystatics/images/%s'%fname,'wb')
                writer.write(body)
                writer.close()
                avatar = fname

            pwd = mymd5(password)
            #dbutil = DBUtil()
            try:
                self.application.dbutil.saveuser(username,pwd,city,avatar)
            except Exception as e:
                if avatar:
                    remove('mystatics/images/%s'%avatar)

                err = str(e) #'duplicate','dberror'
                self.redirect('/regist?msg='+err)
            else:
                self.redirect('/')

        else:
            self.redirect('/regist?msg=empty')

class RegistModule(UIModule):
    def render(self, *args, **kwargs):

        #根据访问参数，提示不同的信息
        #msg=empty,duplicate,dberror
        r = ''
        if  self.request.query:
            err = self.request.query.split('=')[1]
            if err=='empty':
                r = '请输入完整'
            if err=='duplicate':
                r = '用户名重复'
            if err=='dberror':
                r = '数据库错误'

        return self.render_string('mymodule/regist_module.html',
                                  result=r)

