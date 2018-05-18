# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Users(models.Model):
    User_id=models.CharField(max_length=20,primary_key=True)
    Password=models.CharField(max_length=20)
    Wechatid = models.CharField(max_length=20,blank=True)

class Admins(models.Model):
    Adm_account = models.CharField(max_length=20,primary_key=True)
    Adm_password = models.CharField(max_length=20)
    Adm_openid = models.CharField(max_length=20)


class User_infor(models.Model):
    User_id = models.CharField(max_length=20, primary_key=True)
    address = models.CharField(max_length=20)
    pyhonenumber = models.IntegerField(length=11)
    Username = models.CharField(max_length=20)
    Photoprofile = models.CharField(max_length=100)


class Goods_car(models.Model):
    User_id=models.CharField(max_length=20,primary_key=True)
    Goods_id=models.CharField(max_length=10)
    Order_id = models.CharField(max_length=10)


class Order(models.Model):
    User_id=models.CharField(max_length=20,primary_key=True)
    Goods_id=models.CharField(max_length=10)
    Order_id = models.CharField(max_length=10)

