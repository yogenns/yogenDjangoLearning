from django.conf.urls import url
from yogenapp import views

urlpatterns = [
    url('', views.index,name='index')
]