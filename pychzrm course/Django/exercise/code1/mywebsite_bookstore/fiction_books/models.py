from django.db import models

# Create your models here.

class Fictioc_Books(models.Model):
    book_name = models.CharField("书名",max_length=50,default="民谣")
    book_pub = models.CharField("出版社",max_length=30,default="民间流传")
    book_price = models.DecimalField("价格",max_digits=5,decimal_places=2,default=None)
    book_time = models.DateField("上市时间",auto_now_add=True)


# fb = Fictioc_Books()
# fb.book_name = "剑王朝"
# fb.book_price = 288.88
# fb.save()
# fb = Fictioc_Books()
# fb.book_name = "莽荒纪"
# fb.book_price = 289.88
# fb.save()

    # def __str__(self):
    #     return "书名" + self.book_name + "出版社" + self.book_pub
