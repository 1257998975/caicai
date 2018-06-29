from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from caicai import models
from Contor.Class import goods_car
from Contor.Class import orders
from django.core import serializers
import simplejson
from PIL import Image
import uuid
import json


# img=Image.open('d:/dog.png')
# img.show()


# 返回销量最多的菜
def SalesMax(request):
    # oders = models.Order.objects.all().distinct()
    # max = 0
    # for oder in oders:
    #     thisGoodsCount = models.Order.objects.filter(Goods_id=oder.Goods_id).count()
    #     if (max < thisGoodsCount):
    #         max = thisGoodsCount
    #         maxGoods_id = oder.Goods_id
    # data = {"data": models.caicai.objects.get(Goods_id=maxGoods_id)}
    # return HttpResponse(data)
    data = []

    img = open('images/001.jpg')
    print(img.read())

    data.append({"count": 1, "titlr": "分数", "gg": "sfds", "img": json.dumps(img, ensure_ascii=False)})
    data.append({"count": 2, "titlr": "分数", "gg": "sfds"})
    # data = serializers.serialize("json", models.caicai.objects.all())

    return HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type="application/json")


# 返回购物车
def GoodCar(request):
    User_id = request.GET.get('id')
    goods = models.Goods_car.objects.filter(User_id=User_id)
    cars = []
    for good in goods:
        g = models.caicai.objects.get(Goods_id=good.Goods_id)
        price = g.Goods_price * good.Count * g.Discount
        car = {"count": good.Count, "name": g.Goods_name, "picture": g.Goods_picture, "price": price,
               "good_id": g.Goods_id}
        cars.append(car)

    return HttpResponse(simplejson.dumps(cars, ensure_ascii=False), content_type="application/json")


# 返回订单表
def Order(request):
    User_id = request.GET.get('id')
    tabel = []
    order_id = models.Order.objects.filter(User_id=User_id).distinct()
    for order in order_id:
        caicai_id = models.Order.objects.filter(Order_id=order.Order_id)
        for caicai in caicai_id:
            caicai_ = models.caicai.objects.get(Goods_id=caicai.Goods_id)
            data = {"name": caicai_.Goods_name, "picture": caicai_.Goods_picture, "count": caicai.Count,
                    "price": caicai_.Goods_price * caicai_.Discount * caicai.Count, "order_id": caicai.Order_id,
                    "address": caicai.Address, "phone": caicai.Tel,"Status":caicai.Status}
            tabel.append(data)

    return HttpResponse(simplejson.dumps(tabel, ensure_ascii=False), content_type="application/json")


# 取消订单
def DeleteOrder(request):
    try:
        order_id = request.GET.get('Order_id')
        models.Order.objects.filter(Order_id=order_id).delete()
        return HttpResponse(simplejson.dumps(True, ensure_ascii=False), content_type="application/json")
    except:
        return HttpResponse(simplejson.dumps(False, ensure_ascii=False), content_type="application/json")


# 加入购物车
def AddGoodCar(request):
    try:
        User_id = request.GET.get('User_id')
        Good_id = request.GET.get('Good_id')
        Count = request.GET.get('Count')
        models.Goods_car.objects.create(User_id=User_id, Goods_id=Good_id, Order_id=None, Count=Count)
        data = {"Bool": True}
        return HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type="application/json")
    except:
        data = {"Bool": False}
        return HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type="application/json")


# 返回菜品展示
def LookCaiCais(request):
    caicai = models.caicai.objects.all()
    data = []
    for cai in caicai:
        data.append({"Goods_name": cai.Goods_name, "picture": cai.Goods_picture, "Id": cai.Goods_id})
    return HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type="application/json")


# 返回详细菜品展示
def LookCaiCai(request):
    id = request.GET.get('id')
    caicai = models.caicai.objects.get(Goods_id=id)
    data = {"Goods_name": caicai.Goods_name, "picture": caicai.Goods_picture, "Id": caicai.Goods_id,
            "price": caicai.Goods_price, "Discount": caicai.Discount, "pay_for": caicai.Goods_price * caicai.Discount,
            "Reserves": caicai.Reserves, "Goods_count": caicai.Goods_count}
    return HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type="application/json")


# 返回地址
def Adress(request):
    id = request.GET.get('id')
    data = []
    if request.method == 'POST':
        adress = request.GET.get('adress')
        try:
            models.UserRecord.objects.create(id, adress, None, None)
            return HttpResponse(simplejson.dumps(True, ensure_ascii=False), content_type="application/json")
        except:
            return HttpResponse(simplejson.dumps(False, ensure_ascii=False), content_type="application/json")
    else:
        userlist = models.UserRecord.objects.filter(User_id=id)
        for user in userlist:
            da = {"address推荐": user.Address}
            data.append(da)
        return HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type="application/json")


# 返回推荐
def Index(requst):
    id = requst.GET.get('id')
    good_id = models.recommend.objects.get(User_id=id)
    caicai = models.caicai.objects.get(Goods_id=good_id.ReGoods_id)
    data = {"Goods_name": caicai.Goods_name, "picture": caicai.Goods_picture, "Id": caicai.Goods_id,
            "price": caicai.Goods_price, "Discount": caicai.Discount, "pay_for": caicai.Goods_price * caicai.Discount,
            "Reserves": caicai.Reserves, "Goods_count": caicai.Goods_count}
    return HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type="application/json")


# 创建订单
def CreatOrder(requst):
    try:
        user_id = requst.GET.get('User_id')
        address = requst.GET.get('Address')
        tel = requst.GET.get('Tel')
        actual_payment = requst.GET.get('Actual_payment')
        good_car = models.Goods_car.objects.filter(User_id=user_id)
        order_id = uuid.uuid1()
        if not models.UserRecord.objects.get(Address=address):
            models.UserRecord.objects.create(User_id=user_id, Address=address)
        for car in good_car:
            models.Order.objects.create(User_id=user_id, Goods_id=car.Goods_id, Status=0, Order_id=order_id,
                                        Address=address, Tel=tel, Count=car.Count, Actual_payment=actual_payment)
        good_car.delete()
        return HttpResponse(simplejson.dumps(True, ensure_ascii=False), content_type="application/json")
    except:
        return HttpResponse(simplejson.dumps(False, ensure_ascii=False), content_type="application/json")


# 确认收货
def Sure(requst):
    try:
        order_id = requst.GET.get('Order_id')
        order = models.Order.objects.get(Order_id=order_id)
        order.Status = 3
        order.save()
        return HttpResponse(simplejson.dumps(True, ensure_ascii=False), content_type="application/json")
    except:
        return HttpResponse(simplejson.dumps(False, ensure_ascii=False), content_type="application/json")


# 修改购物车
def modify(requst):
    try:
        user_id = requst.GET.get('User_id')
        good_id = requst.GET.get('Good_id')
        count = requst.GET.get('Count')
        cars = models.Goods_car.objects.filter(User_id=user_id)
        for car in cars:
            if car.Goods_id == good_id:
                id=car.id
                break
        models.Goods_car.objects.filter(id=id).update(Count=count)
        return HttpResponse(simplejson.dumps(True, ensure_ascii=False), content_type="application/json")
    except:
       return HttpResponse(simplejson.dumps(False, ensure_ascii=False), content_type="application/json")


# 删除购物车
def Deletecar(requst):
    try:
        user_id = requst.GET.get('User_id')
        good_id = requst.GET.get('Good_id')
        cars = models.Goods_car.objects.filter(User_id=user_id)
        for car in cars:
            if car.Goods_id==good_id:
                id=car.id
                break
        models.Goods_car.objects.filter(id=id).delete()
        return HttpResponse(simplejson.dumps(True, ensure_ascii=False), content_type="application/json")
    except:
        return HttpResponse(simplejson.dumps(False, ensure_ascii=False), content_type="application/json")
