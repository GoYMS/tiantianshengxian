from django.shortcuts import render
from df_user import models as user_models
from df_cart import models as cart_models
# Create your views here.
def order(request):
    id = request.session['user_id']
    user = user_models.UserInfo.objects.get(pk=int(id))
    carts = cart_models.CartInfo.objects.filter(user_id=int(id))
    context = {
        'user':user,
        'carts': carts,
    }
    return render(request,'df_order/order.html/',context)