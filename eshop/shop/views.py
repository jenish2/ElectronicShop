from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Product,ContactUS
from math import ceil
from login.models  import Customer
from cart.models import Ordered

# Create your views here.
def shop(request):
    product = Product.objects.all()
    n=len(product)
    nSlides=n//4 + ceil((n/4)-(n//4))
    print(product)
    return render(request,'eshop.html',{'product':product,'no_of_slides':nSlides ,'range':range(nSlides)})

def laptop(request):
    product = Product.objects.all().filter(catagory='laptop')
    n=len(product)
    nSlides=n//4 + ceil((n/4)-(n//4))
    print(product)
    return render(request,'eshop.html',{'product':product,'no_of_slides':nSlides ,'range':range(nSlides)})

def tv(request):
    product = Product.objects.all().filter(catagory='tv')
    n=len(product)
    nSlides=n//4 + ceil((n/4)-(n//4))
    print(product)
    return render(request,'eshop.html',{'product':product,'no_of_slides':nSlides ,'range':range(nSlides)})

def mobile(request):
    product = Product.objects.all().filter(catagory='mobile')
    n=len(product)
    nSlides=n//4 + ceil((n/4)-(n//4))
    print(product)
    return render(request,'eshop.html',{'product':product,'no_of_slides':nSlides ,'range':range(nSlides)})


def aboutus(request):
    return render(request,'aboutus.html',{})


def productview(request,myid):
    product = Product.objects.all().filter(id=myid)
   # print(product.product_id)
    print(product)
    return render(request,'productview.html',{'product':product})

def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contactus=ContactUS(name=name,email=email,phone=phone,desc=desc)
        contactus.save()
    return render(request,'contactus.html')

def profile(request):
    username=request.session['username']
    print(username)
    un=Customer.objects.all().filter(customer_name=username)
    print(un)
    uo=Ordered.objects.all().filter(user_id=username)
    return render(request,'profile.html',{'un':un,'uo':uo})





def checkout(request):
    return render(request,'checkout.html',{})