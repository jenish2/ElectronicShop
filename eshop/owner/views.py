from django.shortcuts import render
from shop.models import Product,ContactUS
from login.models import Customer
from cart.models import Ordered

def owner(request):
    return render(request,'owner.html',{})

def showQuery(request):
    sq=ContactUS.objects.all()
    print(sq)
    return render(request,'showQuery.html',{'sq':sq})

def showOrder(request):
    so=Ordered.objects.all()
    return render(request,'showOrders.html',{'so':so})

def showUser(request):
    su=Customer.objects.all()
    return render(request,'showUsers.html',{'su':su})

def addProduct(request):
    return render(request,'addProduct.html',{})

def add(request):
    if request.method == 'POST':
        product_number = request.POST['product_number']
        product_name = request.POST['product_name']
        catagory = request.POST['catagory']
        product_discription = request.POST['product_discription']
        img = request.FILES.get('img','a.jpeg')
        price=request.POST['price']
        p=Product(product_number=product_number,product_name=product_name,catagory=catagory,product_discription=product_discription,price=price,img=img)
        p.save()
        messages="Successfully Product Added "
        return render(request,'addProduct.html',{'m':messages})
    else:
        messages="Some Error :Product Not Added"
        return render(request,'addProduct.html',{'m':messages})

def removeProduct(request):
    pl=Product.objects.all()
    return render(request,'removeProduct.html',{'pl':pl})
    
def remove(request,myid):
        product = Product.objects.all().filter(id=myid)
        product.delete()
        pl=Product.objects.all()
        messages="Successfully Deleted Product"
        return render(request,'removeProduct.html',{'m':messages,'pl':pl})
   
