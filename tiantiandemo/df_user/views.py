from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse,HttpResponseRedirect
from hashlib import sha1  #进行加密的包
from . import user_decorator
from df_goods import models
# Create your views here.

def register(request):
    return render(request,'df_user/register.html')

def register_handle(request):
    #接受用户的输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')

    #判断两次密码是否正确

    if upwd!=upwd2:
        return redirect('/user/register/')
    #密码加密
    s1 = sha1()
    s1.update(upwd.encode("utf8"))
    upwd3 = s1.hexdigest()
    #创建对象，存入
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    return redirect('/user/login/')



#判断用户名是否重复
def register_exist(request):
    uname = request.GET.get('uname')
    count=UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})




#登录
def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'df_user/login.html',context)
def login_handle(request):
    #接受请求信息
    post= request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu',0)
    #根据用户名查询对象
    users = UserInfo.objects.filter(uname=uname)
    #判断，如果未查到则用户名错误，如果查到了则判断密码是否正确，正确则转到用户中心
    #因为filter返回的是一个集合，所以可以像下边一样进行判断
    if len(users) == 1:
        s1=sha1()
        s1.update(upwd.encode("utf-8"))
        #判断密码是否正确
        if s1.hexdigest()==users[0].upwd:
            url = request.COOKIES.get('url','/goods/index/')
            red = HttpResponseRedirect(url)
            #下面代码说明是否记住用户名
            if jizhu != 0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id']=users[0].id
            request.session['user_name']=uname
            return red
        else:
            context = {'error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
            return render(request,'df_user/login.html',context)
    else:
        context = {'error_name':1,'error_pwd':0,'uname':uname,'upwd':upwd}
        return render(request,'df_user/login.html',context)

def logout(request):
    del request.session['user_id']  #清除数据
    del request.session['user_name']
    return redirect('/goods/index/')
#个人信息页面
@user_decorator.login   #修饰器(没有登录的话没有办法进行一些操作，会直接转到登录页面)
def info(request):
    user_email = UserInfo.objects.get(id=request.session['user_id']).uemail
    user_uaddress = UserInfo.objects.get(id=request.session['user_id']).uaddress
    #用户浏览
    goods_ids = request.COOKIES.get('goods_ids','')
    goods_ids1 = goods_ids.split(',')
    goods_list = []
    for goods_id in goods_ids1:
        goods_list.append(models.GoodsInfo.objects.get(id=int(goods_id)))

    context = {
        'user_email':user_email,
        'user_uaddress':user_uaddress,
        'user_name':request.session['user_name'],
        'page_name':1,
        'goods_list':goods_list,
    }
    return  render(request,'df_user/user_center_info.html',context)
#订单页面
@user_decorator.login
def order(request):
    return render(request,'df_user/user_center_order.html')
#收货地址页面
@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')
        user.save()
    context = {'user':user}
    return render(request,'df_user/user_center_site.html',context)
