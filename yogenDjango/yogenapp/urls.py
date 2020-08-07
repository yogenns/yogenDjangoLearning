from django.conf.urls import url
from yogenapp import views

urlpatterns = [
    #url('', views.index,name='index'),
    url('formpage/', views.form_page_view,name='form_page'),
    url('signup/', views.signup_view,name='sign_up_page'),
]