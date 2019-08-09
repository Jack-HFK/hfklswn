"""
file : message/models.py
"""
from django.db import models

# Create your models here.
from topic.models import Topic
from user.models import UserProfile


class Message(models.Model):
    content = models.CharField(max_length=90,verbose_name="留言内容")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="留言时间")
    # topic外键
    topic=models.ForeignKey(Topic,verbose_name="Topic外键")
    # user外键
    publisher=models.ForeignKey(UserProfile,verbose_name="UserProfile外键")
    # 区分留言和博客回复 默认为０:留言，　非０:回复
    parent_message=models.IntegerField(default=0,verbose_name="区分留言和回复")

    class Meta:
        db_table = "message"  # 自定义表名

