from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from caicai import models
from Contor.Class import goods_car
from Contor.Class import orders
import simplejson

# 返回销量最多的菜
def SalesMax(request):
    oders = models.Order.objects.all().distinct()
    max = 0
    for oder in oders:
        thisGoodsCount = models.Order.objects.filter(Goods_id=oder.Goods_id).count()
        if (max < thisGoodsCount):
            max = thisGoodsCount
            maxGoods_id = oder.Goods_id
    data = {"data": models.caicai.objects.get(Goods_id=maxGoods_id)}
    return HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type="application/json")


# 返回购物车
def GoodCar(request):
    User_id = request.GET.get('User_id')
    goods = models.Goods_car.objects.filter(User_id=User_id)
    cars=[]
    for good in goods:
        g=goods_car(good.Count,models.caicai.objects.get(Goods_id=good.Goods_id))
        cars.append(g)
    data = {"data": cars}
    return HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type="application/json")



#返回订单表


def Order(request):
    User_id = request.GET.get('User_id')
    tabel=[]
    order_id = models.Goods_car.objects.filter(User_id=User_id).distinct()
    for order in order_id:
        caicaiList=[]
        caicai_id = models.Order.objects.filter(Order_id=order.Order_id)
        for caicai in caicai_id:
            caicaiList.append(models.caicai.objects.filter(Goods_id=caicai.Goods_id))
        orderList=orders(order,caicaiList)
        tabel.append(orderList)
    user_address = models.UserRecord.objects.filter(User_id=User_id)
    data = {"order": tabel,"UserRecord":user_address}
    return HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type="application/json")