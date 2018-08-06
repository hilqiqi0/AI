from django.shortcuts import render
from .models import *
from userinfo.models import *
from memberapp.models import *
from django.db import DatabaseError
import logging
import json
import datetime
from django.http import HttpResponse


# Create your views here.
def add_cart(request):

    #获取前端数据（商品id，商品数量）
    #获取用户id
    #查询
    #存
    #返回
    #
    # 声明一个新的购物车
    # 获取前端数据（商品id,商品数量）
    # 获取用户id
    # 查询用户
    # 查询商品
    # 判断商品是否存在
    # 查询购物车中该用户是否有此商品
    #     商品数量转换成int
    #     如果有加上相应数量商品
    #     没有直接保存
    # 返回页面
    new_cart = CartInfo()
    good_id = request.GET.get('goodid')
    good_count = request.GET.get('gcount')
    user_id = request.session.get('user_id')
    good_ = Goods.objects.filter(id=good_id)
    user_ = UserInfo.objects.get(id=user_id)
    if len(good_) > 0:
        new_cart.user = user_
        new_cart.goods = good_[0]
    else:
        content = {'static':'OK','text':'无该商品'}
        return HttpResponse(json.dumps(content))
        # return render(request,'index.html')
    new_cart.ccount = int(good_count)
    try:
        oldgo = CartInfo.objects.filter(user_id=user_id,goods_id=good_id)
        if len(oldgo) > 0:
            oldgo[0].ccount = oldgo[0].ccount + new_cart.ccount
            oldgo[0].save()
        else:
            new_cart.save()
    except DatabaseError as e:
        logging.warning(e)
    content = {'static': 'OK', 'text': '添加成功'}
    return HttpResponse(json.dumps(content))
    # return render(request,'index.html')


def cart_info(request):
    user_id = request.session.get('user_id')
    find_goods = CartInfo.objects.filter(user_id=user_id)
    return render(request,'cart.html',{'find_goods':find_goods})


def order(request):
    user_id = request.session.get('user_id')
    adss = Address.objects.filter(user_id=user_id)
    content = {"adss":adss}
    return render(request,'order.html',content)


def add_order(request):
    # 获取数据
    # 存数据
    # 返回结果
    user_id = request.session.get('user_id')
    orderdetail = request.POST.get('acot')
    adsname = request.POST.get('adsname')
    adsphone = request.POST.get('adsphone')
    ads = request.POST.get('ads')
    acot = 2
    acount = 22.00
    orderNo = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    print(user_id,orderdetail,adsname,adsphone,ads)
    try:
        user = UserInfo.objects.get(id=user_id)
        order = Order.objects.create(orderNo=orderNo,orderdetail=orderdetail,adsname=adsname,adsphone=adsphone,ads=ads,acot=acot,acount=acount,user=user)
    except DatabaseError as e:
        logging.warning(e)
    content={"static":"OK"}
    return HttpResponse(json.dumps(content))

def delete_cart(request):
    user_id = request.session.get('user_id')
    cart_id = request.GET.get('cart_id')
    try:
        delcart= CartInfo.objects.filter(user_id=user_id,id=cart_id)
        delcart.delete()
    except DatabaseError as e:
        logging.warning(e)
    content={"static":"OK","msg":"删除成功"}
    return HttpResponse(json.dumps(content))
