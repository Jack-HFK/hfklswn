from django.db import models

# Create your models here.

# file: user/models.py

# 此项目不再使用此模型类来记录数据
class User(models.Model):
    username = models.CharField("用户名", max_length=30)
    password = models.CharField("密码", max_length=30)
    # avator = models.CharField('头像')  # 头像 'static/files/meinv.png'

    def __str__(self):
        return "用户" + self.username

