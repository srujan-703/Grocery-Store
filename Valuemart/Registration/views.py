from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as signup,logout as log_out
# Create your views here.
def login(request):
    if request.method=='POST':
        val_username = request.POST.get('username')
        val_password = request.POST.get('password')
        user = authenticate(username=val_username,password=val_password)
        if user is not None:
            signup(request,user)
            request.session['username']=user.username
            request.session['email']=user.email
            fname=user.first_name
            return redirect('/',{'first_name':fname})
        else:
            messages.info(request,'invalid credentials!!')
            return redirect('login')
    else:
        return render(request,'login.html')



def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username=request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken!!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken!!')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user saved!')
                return redirect('login')
        else:
            messages.info(request,'password not matching...')
            return redirect('register')
         
    else:
        return render(request,"register.html")

def logout(request):
    log_out(request)
    return redirect('/')
    