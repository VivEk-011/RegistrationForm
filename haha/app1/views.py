from django.shortcuts import render , redirect
from app1.models import *
from django.views import View
# Create your views here.


def aisehi(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        myemail = request.POST.get('email')
        mypswd = request.POST.get('psd')
        login.objects.create(login_fname = fname,login_lname = lname,login_email=myemail,pswd=mypswd)
        return redirect('index')
    return render(request,'index.html')

def index(request):
    obj = login.objects.all()
    context ={
        'data':obj,
       }
    return render(request,'basi.html',context)

def edit(request,myid):
    obj = login.objects.filter(id=myid).all()
    print(obj)
    if request.method == 'POST':
        fna = request.POST.get('fname')
        lna = request.POST.get('lname')
        ema = request.POST.get('email')
        ps = request.POST.get('psd')

        login.objects.filter(id=myid).update(login_fname=fna,login_lname = lna,login_email=ema,pswd=ps)
        return redirect('index')
    context = {
        'data': obj,
    }    
    return render(request,'edit.html',context)

def destroy(request,myid):
    user = login.objects.get(id=myid)
    user.delete()
    return redirect('index')
    

