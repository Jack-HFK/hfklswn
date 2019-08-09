"""
    file : topic/models.py
"""
from django.db import models

# Create your models here.
from user.models import UserProfile


class Topic(models.Model):
    title = models.CharField(verbose_name="文章主题",max_length=50)
    # "tec" - 技术类 "no-tec" -非技术类
    category = models.CharField(verbose_name="博客的分类",max_length=20)
    #　"public" - 公开的   "private"   - 私有的
    limit = models.CharField(verbose_name="权限",max_length=10)
    introduce = models.CharField(verbose_name="博客简介",max_length=90)
    content = models.TextField(verbose_name="博客内容")
    created_time = models.DateTimeField(verbose_name="博客创建时间", auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name="博客修改时间",auto_now=True)
    # 设置外键
    author = models.ForeignKey(UserProfile)


    class Meta:
        db_table = "topic" # 自定义表名