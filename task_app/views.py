from django.shortcuts import  render, redirect
from .forms import MyUserForms
from .models import MyUser
from django.contrib.auth import login
from .models import *
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login,logout

# Create your views here.
def home(request):
    product=Product.objects.all()
    context={
        "product":product
    }
    return render(request,'home.html',context)

def show(request):
    return render(request,'show.html')

class Registration(View):
    def get(self,request):
        myforms=MyUserForms()
        return render(request,'register.html',{"userform":myforms})    
    def post(self,request):
        myforms=MyUserForms(request.POST)
        if myforms.is_valid():
                myforms.save()
                return render(request,'login.html')


class Logins(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        unm=request.POST['unm']
        passd=request.POST['pass']
        user_varify=MyUser.objects.filter(username=unm).filter(password=passd)
        if user_varify:
            return render(request,'home.html')
        else:
           return render(request,'register.html')


def logouts(request):
    logout(request)
    return redirect('home')

def delete(request):
    d_id=request.GET.get('d_id')
    Product.objects.get(id=d_id).delete()
    return redirect('home')


def update(request):
    if request.method=="GET":
        d_id=request.GET.get('d_id')
        product=Product.objects.filter(id=d_id)
        return render(request,'update.html',{'product':product})
    else:
        
        d_id=request.POST.get('d_id')
        print(d_id,"...............")
        product=Product.objects.get(id=d_id)
        product.name=request.POST.get('name')
        product.descriptions=request.POST.get('descriptions')
        product.price=request.POST.get('price')
        product.save()
        return redirect('home')


def add_product(request):
    if request.method=="POST":
        product=Product()
        product.name=request.POST.get('name')
        product.descriptions=request.POST.get('descriptions')
        product.price=request.POST.get('price')
        product.save()
        return redirect('home')
    return render(request, 'add.html')