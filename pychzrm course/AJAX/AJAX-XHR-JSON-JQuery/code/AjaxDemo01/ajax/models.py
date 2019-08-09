"""
    file:ajax/models.py
"""
from django.db import models

# Create your models here.


class Users(models.Model):
    uname = models.CharField("用户名",max_length=68,unique=True)
    upwd = models.CharField("用户密码",max_length=16)
    uemail = models.EmailField("电子邮箱")
    nickname = models.CharField("昵称",max_length=35)

    def __str__(self):
        return "用户名" + self.uname + "密码" + self.upwd

