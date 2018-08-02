from django.db import models

# 声明自定的objects - models.Manager
class AuthorManager(models.Manager):
    #添加自定义函数　－　查询Author表中共有多少条数据
    def auCount(self):
        return self.all().count()
    #查询年纪小于指定年纪的作者的信息
    def lt_age(self,age):
        return self.filter(age__lt=age)

class BookManager(models.Manager):
    #添加函数，查询书名中包含指定关键字的书籍的信息
    def titleContains(self,keywords):
        return self.filter(title__contains=keywords)


# Create your models here.
class Publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    website=models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        db_table='publisher'
        verbose_name='出版社'
        verbose_name_plural=verbose_name

#创建Book模型类
#title,书名,publicate_date出版时间
class Book(models.Model):
    #重新指定objects
    objects = BookManager()
    title = models.CharField(max_length=50,verbose_name='书名')
    publicate_date = models.DateField(verbose_name='出版时间')
    # 增加对Publisher的引用(1:M)
    publisher = models.ForeignKey(Publisher,verbose_name='出版社',null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table='book'
        verbose_name='书籍'
        verbose_name_plural=verbose_name
        ordering=['-publicate_date']


#创建Author模型类，
#name,姓名，age,年龄,email,邮箱
class Author(models.Model):
    # 使用AuthorManager覆盖当前的objects
    objects = AuthorManager()
    names = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(null=True)
    #增加一个状态列，来表示用户是启用的还是禁用的，默认为True表示启用
    isActive = models.BooleanField(default=True)
    #增加对Book的多对多的引用
    book = models.ManyToManyField(Book)
    #增加对Publisher的多对多的引用
    publisher = models.ManyToManyField(Publisher)

    def __str__(self):
        return self.names

    # 声明内部类，来定义当前类在管理页面中的展现形式
    class Meta:
            # 1.修改当前表名为 author
            db_table='author'
            # 2.修改实体类在后台管理页中的名称(单数)
            verbose_name='作者'
            # 3.修改实体类在后台管理页中的名称(复数)
            verbose_name_plural = verbose_name
            # 4.首先按照年龄降序排序，其次按照ＩＤ升序排序
            ordering = ['-age','id']



class Wife(models.Model):
    names = models.CharField(max_length=30)
    age = models.IntegerField()
    # 增加一对一的引用，引用自Author实体
    author = models.OneToOneField(Author,null=True)

    def __str__(self):
        return self.names

    class Meta:
            db_table='wife'
            verbose_name='夫人'
            verbose_name_plural = verbose_name
