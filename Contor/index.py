from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from caicai import models




def classify(requst):
    oders=models.Order.objects.all().distinct()
    max=0
    for oder in oders:
        thisGoodsCount=models.Order.objects.filter(Goods_id=oder.Goods_id).count()
        if(max<thisGoodsCount):
            max=thisGoodsCount
            maxGoods_id=oder.Goods_id
    caicai=models.caicai.objects.get(Goods_id=maxGoods_id)
    tp = loader.get_template("Index.html")
    html = tp.render({"users": caicai})
    return HttpResponse(html)