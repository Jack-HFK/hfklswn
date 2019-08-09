from django.contrib import admin

# Register your models here.

# file:bookstore/admin.py

# 在应用app中的admin.py中导入注册要管理的模型models类
from . import models

# 调用 admin.site.register 方法进行注册
admin.site.register(models.Book)
admin.site.register(models.Author)

# 编写模型管理器类
class BookManager(admin.ModelAdmin):
    list_display = ["id","title","pub","price"]
    list_display_links = ["id","title",]
    list_filter = ["pub"]
    search_fields = ["title","pub"]
    list_editable = ["price","pub",]
    pass


admin.site.register(models.Book,BookManager)
admin.site.register(models.Author)

# list_display去控制哪些字段会**显示**在Admin 的修改列表页面中。
# st_display_links** 可以控制list_display中的字段是否应该**链接**到对象的“更改”页面。
# st_filter** 设置激活激活Admin 修改列表**页面**右侧栏中的**过滤器**。
# arch_fields** 设置启用Admin 更改列表**页面**上的**搜索框。**
# st_editable** 设置为模型上的**字段名称列表*这将允许在更改列表页面上进行**编辑**。