from caicai.models import Users
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
def ddd(requst):
    User=Users.objects.all()
    tp = loader.get_template("Index.html")
    html = tp.render({"users": User})
    return HttpResponse(html)