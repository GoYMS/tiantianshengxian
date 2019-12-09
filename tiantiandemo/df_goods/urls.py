from django.conf.urls import include, url
from django.contrib import admin
from df_user import urls
from df_goods import views
urlpatterns = [
    #首页
    url(r'^index/$',views.index),
    #列表页
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.list),
    #详情页
    url(r'^(\d+)/$',views.detail)



]
