"""
    file : user/models.py
"""
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    username = models.CharField("用户名",max_length=11,primary_key=True)
    nickname = models.CharField("用户昵称",max_length=30)
    email = models.EmailField("用户邮箱",max_length=64)
    password = models.CharField("用户密码",max_length=64)
    sign = models.CharField("个人签名",max_length=50,null=True)
    info = models.CharField("个人描述",max_length=150,null=True)
    avatar = models.ImageField("头像字段",upload_to="avatar/",null=True)
    score = models.ImageField("分布式锁测试分数",null=True,default=0)

    # 类名不可改变
    class Meta:
        db_table = "user_profile"   # 自定义表名


    def __str__(self):
        return "用户名:%s,用户邮箱:%s,用户密码:%s,"%(self.username,self.email,self.password)
