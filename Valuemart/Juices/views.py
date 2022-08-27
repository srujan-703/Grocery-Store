from django.shortcuts import redirect, render
from HOME.models import item
from django.views import View
# Create your views here.
class Juices(View):
    def post(self,request):
        item=request.POST.get('item')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(item)
            if quantity:
                if remove:
                    if quantity==1:
                        cart.pop(item)
                    else:
                        cart[item]=quantity-1
                else:
                    cart[item]=quantity+1
            else:
                cart[item]=1
        else:
            cart={}
            cart[item] =1
        request.session['cart']=cart
        return redirect('juices')
           
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        itms= item.get_all_juices();
        return render(request,"juices.html",{'items' : itms})