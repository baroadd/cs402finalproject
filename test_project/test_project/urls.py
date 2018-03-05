
from django.conf.urls import url
from sql_checkingapp import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^$/(?P<url>.*)',views.getparams),
]
