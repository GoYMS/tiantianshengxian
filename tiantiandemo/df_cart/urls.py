from django.conf.urls import include, url
from django.contrib import admin
from df_cart import views

urlpatterns = [
   url(r'^cart/$',views.cart),
   #第一个代表商品编号，第二个代表数量
   url(r'^add(\d+)_(\d+)/$',views.add),
   #增加商品数量
   url(r'^edit(\d+)_(\d+)/$',views.edit),
   #删除商品
   url(r'^delete(\d+)/$',views.delete),
]
