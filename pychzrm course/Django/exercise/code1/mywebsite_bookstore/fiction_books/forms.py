"""
file : fiction_books/forms.ppy
"""

from django import forms

class Forms1(forms.Form):
    fiction_book_name = forms.CharField(max_length=30,label="输入书名")
    fiction_book_price = forms.DecimalField(max_digits=5,decimal_places=2)
