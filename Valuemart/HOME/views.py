from django import views
from django.shortcuts import render
from django.views.generic.base import View
from .models import item
# Create your views here.
def index(request):
    print(request.session.get('username'))
    print('hey:',request.session.get('cart'))
    return render(request,"index.html")

class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        items=item.get_items_by_id(ids)
        print(items)
        return render(request,'cart.html',{'items' : items})