"""
    file:users/models.py
    用户模型
"""
from django.db import models


# Create your models here.

class UserIntro(models.Model):
    username = models.CharField(verbose_name="用户姓名",
                                max_length=11,
                                primary_key=True)
    nickname = models.CharField(verbose_name="昵称", max_length=30, default=username)
    email = models.EmailField(verbose_name="邮箱", max_length=50)
    password = models.CharField(verbose_name="密码", max_length=64)
    sign = models.CharField(verbose_name="个人签名", max_length=50, null=True)
    info = models.CharField(verbose_name="个人描述", max_length=150, null=True)
    avatar = models.ImageField(verbose_name="头像", upload_to="avatar/", null=True)

    def __str__(self):
        return "用户名：" + self.username + "密码：" + self.password + "邮箱：" + self.email

    class Meta:
        db_table = "users_intro"
