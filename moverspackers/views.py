from distutils.log import error
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user  = authenticate(username = u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    return render(request,'admin_login.html',locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')

def Logout(request):
    logout(request)
    return redirect(index)

def add_services(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == "POST":
        st = request.POST['servicetitle']
        des = request.POST['description']
        image = request.FILES['image']

        try:
            Services.objects.create(title = st,description=des,image=image)
            error = "no"
        except:
            error="yes"
    return render(request,'add_services.html',locals())

def manage_services(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    services = Services.objects.all()

    return render(request,'manage_services.html',locals())

def edit_service(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    service = Services.objects.get(id = pid)
    if request.method == "POST":
        st = request.POST['servicetitle']
        des = request.POST['description']


        service.title = st
        service.description = des

        try:
            service.save()
            error = "no"
        except:
            error = "yes"
        try:
            image = request.FILES['image']
            service.image = image
            service.save()
        except:
            pass

    return render(request,'edit_service.html',locals())

def delete_service(request,pid):
    service = Services.objects.get(id = pid)
    service.delete()
    return redirect('manage_services')

def services(request):
    services = Services.objects.all()
    return render(request,'services.html',locals())