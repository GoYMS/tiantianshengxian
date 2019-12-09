from django.db import models
import df_user
import df_goods
# Create your models here.
class CartInfo(models.Model):
    #与用户相关
    #django 升级到2.0之后,表与表之间关联的时候,必须要写on_delete参数,否则会报异常
    user = models.ForeignKey('df_user.UserInfo',on_delete=models.CASCADE)
    #与商品相关
    goods = models.ForeignKey('df_goods.GoodsInfo',on_delete=models.CASCADE)

    count = models.IntegerField(max_length=300)