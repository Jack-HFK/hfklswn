from django.db import models

# Create your models here.

# file:bookstore/models
class Book(models.Model):
    title = models.CharField('书名', max_length=50,default="")
    pub = models.CharField('出版社', max_length=50,default="")
    price = models.DecimalField('定价', max_digits=7,
                                decimal_places=2,
                                default=0.0)
    market_price = models.DecimalField("零售价",max_digits=7,
                                       decimal_places=2,
                                       default=9999)
    pub_date = models.DateField('出版时间',
                                # default='2017-1-1'
                                auto_now_add=True
                                # auto_now=True
                                )
    #　类方法输出时转为以下格式的字符串
    def __str__(self):
        return "书名" + self.title + "出版社" + self.pub

class Author(models.Model):
    name = models.CharField("姓名",unique=True,
                            db_index=True,
                            max_length=50)
    age = models.IntegerField("年龄",default=1)
    email = models.EmailField("邮箱",null=True)