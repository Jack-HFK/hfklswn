from django.conf.urls import url

from . import views
# file:templates/urls

urlpatterns = [
    url(r"page1",views.page1_view)

]