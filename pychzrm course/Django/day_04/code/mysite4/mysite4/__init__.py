# file: mysite4/__init__.py

import pymysql

# 让Django 支持MySQL
pymysql.install_as_MySQLdb()