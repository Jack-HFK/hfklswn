from django.db import models

# Create your models here.
class Users(models.Model):
  uname = models.CharField("用户名称",max_length=30)
  upwd = models.CharField("用户密码",max_length=30)
  uemail = models.EmailField("电子邮箱")
  nickname = models.CharField("用户昵称",max_length=30)
