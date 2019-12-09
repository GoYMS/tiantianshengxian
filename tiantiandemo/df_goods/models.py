from django.db import models
from tinymce.models import HTMLField
# Create your models here.
#商品类型
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default = False)
    def __str__(self):
        return self.ttitle

#商品
class GoodsInfo(models.Model):
    #标题
    gtitle = models.CharField(max_length=20)
    #图片
    gpic = models.ImageField(upload_to='df_goods')
    #价格
    gprice = models.DecimalField(max_digits=5,decimal_places=2)#第一个参数代表最高几位，后一个代表小数点后几位
    isDelete = models.BooleanField(default=False)
    #重量单位
    gunit = models.CharField(max_length=20,default='500g')
    #人气
    gclick = models.IntegerField()
    #简介
    gjianjie = models.CharField(max_length=200)
    #库存
    gkucun = models.IntegerField()
    #商品详情
    gcontent =HTMLField()

    # 外键
    gtype = models.ForeignKey(TypeInfo,on_delete=models.CASCADE)
    def __str__(self):
        return self.gtitle