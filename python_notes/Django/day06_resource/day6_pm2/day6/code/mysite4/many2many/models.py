from django.db import models

# Create your models here.

# file: many2many/models.py


# many2many_author3
class Author3(models.Model):
    name = models.CharField('姓名', max_length=30)
    # books = models.ManyToManyField(Book3)

    def __str__(self):
        return "作者：" + self.name

# many2many_book3
class Book3(models.Model):
    title = models.CharField('书名', max_length=50)
    # 多对多的关联属性
    authors = models.ManyToManyField(Author3)
    def __str__(self):
        return "书名：" + self.title


