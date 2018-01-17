from django.conf.urls import url
from . import views

app_name='ok'

urlpatterns = [
    url(r'^home/products/$', views.index, name='index'),
    url(r'^home/products/sort/$', views.sort, name='sort'),
    url(r'^home$', views.home, name='home'),
    url(r'^home/login/$', views.login_next, name='login_next'),
    url(r'^home/login/a/$', views.addRow, name='a'),
    url(r'^home/products/(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.loginpage,name='login'),
]