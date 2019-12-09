from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.

#首页

def index(request):
    #查询各分类的最新四条，最热四条数据
    typelist = TypeInfo.objects.all()
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
    context = {
        'type0':type0,'type01':type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
        'type5': type5, 'type51': type51,
    }

    return render(request,'df_goods/index.html',context)

#列表页
def list(request,tid,pindex,sort):   #tid 商品类型  pindx 页数  sort 分类排序类型
    id = int(tid)
    typeinfo = TypeInfo.objects.get(pk=id)
    #列表页左侧的新品推荐
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort == '1': #默认为最新
        goods_list = GoodsInfo.objects.filter(gtype_id=id).order_by('-id')
    if sort == '2': #价格
        goods_list = GoodsInfo.objects.filter(gtype_id=id).order_by('-gprice')
    if sort == '3': #人气，点击量
        goods_list = GoodsInfo.objects.filter(gtype_id=id).order_by('-gclick')
    #分页器
    paginator = Paginator(goods_list,10)
    page = paginator.page(int(pindex))
    context = {
        'page':page,
        'paginator':paginator,
        'typeinfo':typeinfo,
        'sort':sort,
        'news':news,
    }
    return render(request,'df_goods/list.html',context)


#详细页
def detail(request,id):
    goods = GoodsInfo.objects.get(pk=int(id))
    goods.gclick = goods.gclick+1  #每访问一次，访问量加一
    goods.save()  #保存
    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]   #最新的两条数据
    context = {
        'title':goods.gtype.ttitle,
        'goods':goods,
        'news':news,
        'id':id,
    }
    response = render(request,'df_goods/detail.html',context)

#记录最近浏览，在用户中心使用
    goods_ids  = request.COOKIES.get('goods_ids','')
    goods_id = '%d'%goods.id
    if goods_ids != '':  #判断是否有浏览记录，如果有则继续判断
        goods_ids1 = goods_ids.split(',')  #拆分为列表
        if goods_ids1.count(goods_id)>=1: #如果商品已经被记录，则删除
            goods_ids1.remove(goods_id)
        goods_ids1.insert(0,goods_id) #添加到第一个
        if len(goods_ids1)>=6: #如果查过6个，则删除第一个
            del goods_ids1[5]
        goods_ids = ','.join(goods_ids1)  #拼接为字符串
    else:
        goods_ids = goods_id  #如果没有浏览记录直接加
    response.set_cookie('goods_ids',goods_ids) #写入cookie
    return response