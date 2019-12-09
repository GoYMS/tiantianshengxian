from django.db import models

# Create your models here.
class OrderInfo(models.Model):
    oid = models.CharField(max_length=20,primary_key=True)
    #用户
    user = models.ForeignKey('df_user.UserInfo',on_delete=models.CASCADE)
    #创建的时间
    odate = models.DateTimeField(auto_now=True)
    #是否支付
    oIsPay = models.BooleanField(default=False)
    #总共的商品
    ototal = models.DecimalField(max_digits=6,decimal_places=2)
    #地址
    oaddress = models.CharField(max_length=200)

#详细表
class OrderDetailInfo(models.Model):
    goods = models.ForeignKey('df_goods.GoodsInfo',on_delete=models.CASCADE)
    order = models.ForeignKey(OrderInfo,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    count = models.IntegerField()