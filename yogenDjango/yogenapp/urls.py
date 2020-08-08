from django.conf.urls import url
from yogenapp import views

#TEMPLATE URLS
app_name = 'yogenapp'

urlpatterns = [
    #url('', views.index,name='index'),
    url('formpage/', views.form_page_view,name='form_page'),
    url('signup/', views.signup_view,name='sign_up_page'),
    url('register/', views.register_view,name='register'),
    url('user_login/', views.user_login,name='user_login'),
]
