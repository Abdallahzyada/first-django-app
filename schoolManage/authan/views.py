from django.shortcuts import render ,reverse
from django.urls import reverse_lazy
from django.shortcuts import *
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def Login(req):
    context = {}
    context['form'] = Loginform()
    if(req.method=='POST'):
        username=req.POST['username']
        password=req.POST['password']
        obj=MYUser.objects.filter(username=username,password=password)
        authobj=authenticate(username=username,password=password)
        if(len(obj)>0 and authobj is not None):
            req.session['id']=obj[0].id
            req.session['name']=obj[0].username
            login(req,authobj)
            return redirect(reverse('trainee_list'))
        else:
            context['msg']='invalid cred'
    return render(req, 'authan/login.html', context)

def Logout(req):
    req.session.clear()
    return redirect(reverse('login'))


def Register(req):
    context = {}
    context['form']= Regsitrationform()

    if(req.method=='POST'):
        f=Regsitrationform(req.POST)
        if(f.is_valid()):
            f.save()#store user account_myuser
            User.objects.create_user(username=req.POST['username'],password=req.POST['password'])


    # if(req.method=='POST'):
    #     f=Regform(req.POST)
    #     if(f.is_valid()):
    #         f.save()
    return render(req,'authan/register.html'  ,context)