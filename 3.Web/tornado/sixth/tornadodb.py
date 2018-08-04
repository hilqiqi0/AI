import hashlib
import json
from os import remove

import pymysql
import time

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_config_file
from tornado.web import Application, RequestHandler, UIModule

from day04.util.myutil import mymd5


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

        #step1　通过pymysql建立与数据库的联接
        settings={'host':'127.0.0.1',
                  'port':3306,
                  'user':'root',
                  'password':'123456',
                  'database':'blog_db',
                  'charset':'utf8'}
        connection = pymysql.connect(**settings)

        #step2 通过联接获取游标
        cursor = connection.cursor()

        #step3 利用游标发送SQL语句
        #这么写sql,可能会被注入攻击
        # sql = 'select count(*) from tb_user ' \
        #       'where user_name="%s" and ' \
        #       'user_password="%s"'%(username,password)

        sql = 'select count(*) ' \
              'from tb_user ' \
              'where user_name=%s ' \
              'and user_password=%s'

        pwd = mymd5(password)

        params=(username,pwd)
        cursor.execute(sql,params)

        #step4 如果有需要，利用cursor获取数据库结果
        #result = cursor.fetchall()#((1,),)
        result = cursor.fetchone()#(10,)
        if result[0]:
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

            settings={'host':'127.0.0.1',
                      'port':3306,
                      'user':'root',
                      'password':'123456',
                      'database':'blog_db',
                      'charset':'utf8'}
            connection = pymysql.connect(**settings)
            cursor = connection.cursor()
            sql='insert into tb_user(' \
                'user_name, ' \
                'user_password, ' \
                'user_avatar, ' \
                'user_city) ' \
                'values(%s,%s,%s,%s)'

            #将原始的pasword利用摘要算法(md)进行格式的转换
            # md = hashlib.md5()
            # md.update(password.encode('utf8'))
            # pwd = md.hexdigest()
            pwd = mymd5(password)

            params = (username,pwd,avatar,city)
            try:
                cursor.execute(sql,params)
                #提交！！！
                cursor.connection.commit()
            except Exception as e:
                if avatar:
                    remove('mystatics/images/%s'%avatar)

                err = str(e)
                #(1062, "Duplicate entry 'abc' for key 'user_name'")
                code = err.split(',')[0].split('(')[1]
                r=''
                if code == '1062':
                    r = 'duplicate'
                else:
                    r = 'dberror'

                self.redirect('/regist?msg='+r)
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


define('duankou',type=int,default=8888)
parse_config_file('../config/config')
app = Application(handlers=[('/',IndexHandler),
                            ('/login',LoginHandler),
                            ('/blog',BlogHandler),
                            ('/regist',RegistHandler)],
                  template_path='mytemplate',
                  static_path='mystatics',
                  ui_modules={'loginmodule':LoginModule,
                              'blogmodule':BlogModule,
                              'registmodule':RegistModule})
server = HTTPServer(app)
server.listen(options.duankou)
IOLoop.current().start()