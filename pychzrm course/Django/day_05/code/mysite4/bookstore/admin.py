from django.contrib import admin

# Register your models here.

# file: bookstore/admin.py

from . import models

class BookManager(admin.ModelAdmin): # 编写模型管理器类
    list_display = ['id', 'title', 'pub', 'price', 'pub_date', 'market_price']
    list_display_links = ['id', 'title', 'pub']
    list_filter = ['pub']
    search_fields = ['title', 'pub']
    list_editable = ['price']
    pass


admin.site.register(models.Book, BookManager)
admin.site.register(models.Author)
admin.site.register(models.Wife)

