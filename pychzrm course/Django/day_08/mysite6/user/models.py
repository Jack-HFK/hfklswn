from django.db import models

# Create your models here.

# file : user/models.py

# 此项目为自定义用户名与密码检测系统
class User(models.Model):
    username = models.CharField("用户名",max_length=30)
    password = models.CharField("密码",max_length=30)

    def __str__(self):
        return "用户名 :"  + self.username +" "+ "密码 : " + self.password