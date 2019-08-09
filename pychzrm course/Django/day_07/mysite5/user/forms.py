# file:user/forms.py
from django import forms

class Reg2(forms.Form):
    username = forms.CharField(max_length=30,label="请输入用户名")
    password = forms.CharField(max_length=38,label="请输入密码",
                               widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=38,label="请再次输入密码")