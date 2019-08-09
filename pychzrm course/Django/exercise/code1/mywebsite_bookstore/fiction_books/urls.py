#  file:fiction_books/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^zhuxian$",views.zhuxian_view),
    url(r"^models_class$",views.models_class),
    url(r"^forms$",views.fiction_books_forms),
]



