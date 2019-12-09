from django.db import models

# Create your models here.
class UserInfo(models.Model):
    #用户名
    uname = models.CharField(max_length=20)
    #密码
    upwd = models.CharField(max_length=40)
    #邮箱
    uemail = models.CharField(max_length=30)
    #收件人
    ushou = models.CharField(max_length=20,default='')
    #地址
    uaddress = models.CharField(max_length=100,default='')
    #邮编
    uyoubian = models.CharField(max_length=6,default='')
    #手机号
    uphone = models.CharField(max_length=11,default='')
   #dafault ,blank 是Python层面的约束，不影响数据库