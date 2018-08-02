from django.db import models

# Create your models here.
# 创建商品类型　Models
class GoodsType(models.Model):
    title = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='static/upload/goodstype')
    desc = models.CharField(max_length=100)

#创建商品　Models
class Goods(models.Model):
    title = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    spec = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='static/upload/goods')
    isActive = models.BooleanField(default=True)
    #增加对GoodsType的引用(1:M)
    goodsType = models.ForeignKey(GoodsType,null=True)

#创建用户　Models
class Users(models.Model):
    uphone = models.CharField(max_length=11)
    upwd = models.CharField(max_length=20)
    uemail = models.EmailField(null=True)
    uname = models.CharField(max_length=20)
    isActive = models.BooleanField(default=True)
