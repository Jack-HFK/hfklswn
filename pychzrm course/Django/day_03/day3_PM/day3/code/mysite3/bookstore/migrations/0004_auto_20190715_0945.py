# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-15 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_book_pub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub',
            field=models.CharField(default='清华大学出版社', max_length=50, verbose_name='出版社'),
        ),
    ]