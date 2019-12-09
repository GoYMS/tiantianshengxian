from django.conf.urls import include, url
from django.contrib import admin
from df_user import urls as user_urls
from df_goods import urls as goods_urls
from df_cart import urls as cart_urls
from df_order import urls as order_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'test6.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^user/',include(user_urls)),
    url(r'^goods/',include(goods_urls)),
    url(r'^tinymce/',include('tinymce.urls')),
    url(r'^cart/',include(cart_urls)),
    url(r'^order/',include(order_urls)),


]
