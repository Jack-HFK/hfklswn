from django.db import models

# Create your models here.

# file: bookstore/models.py

class Book(models.Model):
    title = models.CharField('书名', max_length=50,
                             default='')
    pub = models.CharField('出版社', max_length=50,
                           default='清华大学出版社')
    price = models.DecimalField('定价', max_digits=7,
                                decimal_places=2,
                                default=0.0)
    pub_date = models.DateField('出版时间',
                                # default='2017-1-1'
                                # auto_now_add=True
                                auto_now=True
                                )

