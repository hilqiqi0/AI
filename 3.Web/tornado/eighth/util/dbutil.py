import pymysql


class DBUtil:
    def __init__(self,**kwargs):
        #获取数据库联接参数
        #建立与数据库的联接
        #k1=v1,k2=v2,k3=v3
        #kwargs{'k1':v1,'k2':v2,'k3':v3}
        #kwargs['k1']
        #kwargs['k2']
        #kwargs['k3']
        # settings = {'host': '127.0.0.1',
        #             'port': 3306,
        #             'user': 'root',
        #             'password': '123456',
        #             'database': 'blog_db',
        #             'charset': 'utf8'}
        user = kwargs.get('user','root')
        password = kwargs.get('password','123456')
        host = kwargs.get('host','127.0.0.1')
        port = kwargs.get('port',3306)
        database = kwargs.get('database','blog_db')
        charset = kwargs.get('charset','utf8')
        connection = pymysql.connect(user=user,
                                     password=password,
                                     host=host,
                                     port=port,
                                     database=database,
                                     charset=charset)
        if connection:
            self.cursor = connection.cursor()
        else:
            raise Exception('数据库连接参数有误！')

    def isloginsuccess(self,username,password):
        #根据输入的用户名和密码
        #判定用户登录是否成功
        sql='select count(*) from tb_user ' \
            'WHERE user_name=%s and user_password=%s'
        params=(username,password)
        self.cursor.execute(sql,params)
        result = self.cursor.fetchone()
        if result[0]:
            return True
        else:
            return False


    def saveuser(self,username,password,city,avatar):
        #根据用户输入的信息
        #完成用户注册
        sql='insert into tb_user(user_name, ' \
                                'user_password, ' \
                                'user_avatar, ' \
                                'user_city) ' \
                                'values(%s,%s,%s,%s) '
        params=(username,password,avatar,city)
        try:
            self.cursor.execute(sql,params)
            self.cursor.connection.commit()
        except Exception as e:
            #duplicate,dberror
            #(1062,'duplicate entry.....)
            err = str(e)
            r='dberror'
            code = err.split(',')[0].split('(')[1]
            if code=='1062':
                r='duplicate'
            raise Exception(r)

    def getblogs(self):
        #取出数据库中与博客相关的内容
        #并组织成正确的数据格式

        sql='''select user_name,user_avatar,blog_title,blog_content,tc,c

from (
        select comment_blog_id,count(*)c 
        from tb_comment
        group by comment_blog_id
     )t3

right join ( 
       
       select user_name,user_avatar,blog_id,blog_title,blog_content,tc

from tb_user

join (
     select blog_id,blog_title,blog_content,tc,blog_user_id
     from tb_blog
     left join (
       select rel_blog_id, group_concat(tag_content)tc
       from tb_tag
       join (
           select rel_blog_id,rel_tag_id
           from tb_blog_tag
          )t
       on tag_id = rel_tag_id
       group by rel_blog_id
         )t1
     on blog_id = rel_blog_id

     )t2
on user_id = blog_user_id


     )t4

on comment_blog_id = blog_id'''
        self.cursor.execute(sql)
        result = self.cursor.fetchall()#((),(),())
        print('博客：－－－－－>',result[0])
        blogs=[]
        #('abc',
        # None,
        # '第一篇博客',
        # '哈哈哈，今天星期三，开心的一天',
        # '体育,教育,财经',
        # 5)
        for b in result:
            blog={}
            blog['author']=b[0]
            blog['avatar']=b[1]
            blog['title']=b[2]
            blog['content']=b[3]
            if b[4]:
                blog['tags']=b[4]
            else:
                blog['tags'] = ''
            blog['count']=b[5]
            blogs.append(blog)

        return blogs

    def isexists(self,username):
        #根据传入的用户名判断该用户是否已存在
        sql ='select count(*) from tb_user ' \
             'WHERE user_name=%s '
        params = (username,)
        self.cursor.execute(sql,params)
        result = self.cursor.fetchone()
        if result[0]:
            #用户表中已经存在叫该用户名的用户
            return True
        else:
            #用户表中不存在叫该用户名的用户
            return False

    def getavatar(self,username):
        #根据用户名在数据表中查询该用户名对应的头像
        sql='select user_avatar from tb_user ' \
            'WHERE user_name=%s'
        params=(username,)
        self.cursor.execute(sql,params)
        #（xxxxx.png,）(None,) None
        result = self.cursor.fetchone()
        #如果输入的用户名根本不在用户表中
        #result本身就是None
        if result:
            if result[0]:
                return result[0]
            else:
                return 'default_avatar.png'
        else:
            return 'default_avatar.png'

