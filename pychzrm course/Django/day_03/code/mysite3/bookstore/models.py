from django.db import models

# Create your models here.

# file:bookstore/models
class Book(models.Model):
    title = models.CharField("书名",max_length=50)
