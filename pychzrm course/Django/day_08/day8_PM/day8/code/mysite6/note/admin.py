from django.contrib import admin

# Register your models here.

# file : note/admin.py

from .models import Note

admin.site.register(Note)
