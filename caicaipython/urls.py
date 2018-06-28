"""caicaipython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Contor import index
from recommendSystem import mainControl

urlpatterns = [
    url(r'^SalesMax/', index.SalesMax),
    url(r'^GoodCar/', index.GoodCar),
    url(r'^AddGoodCar/', index.AddGoodCar),
    url(r'^Order/', index.Order),
    url(r'^Delete/', index.DeleteOrder),
    url(r'^Lookcaicais/', index.LookCaiCais),
    url(r'^Lookcaicai/', index.LookCaiCai),
    url(r'^index/', index.Index),
    url(r'^address/', index.Adress),
    url(r'^Sure/', index.Sure),
    url(r'^CreatOrder/', index.CreatOrder),
    url(r'^modify/', index.modify),
    url(r'^Decar/', index.Deletecar),
]
