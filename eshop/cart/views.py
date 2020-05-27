from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from cart.models import Order,Ordered
from shop.models import Product


def cart(request):
    try:
        u=request.session['username']
        print(u)
        total = 0
        cartdata = Order.objects.filter(user_id=request.session['username'])
        for i in cartdata:
            total = total + i.quantity * i.price
        print(cartdata)
        if total == 0:
            return render(request, 'cart.html', {'msg': 'Your Cart is Empty', 'total': total})
        else:
            return render(request, 'cart.html', {'cart': cartdata, 'total': total})
    except KeyError:
        return render(request, 'login.html', {'msg': 'Login to view your Cart!'})


def pay(request):
    return render(request, 'payment.html')


def bill(request):
    total = 0
    username = request.session['username']
    bill = Order.objects.filter(user_id=username)
    for i in bill:
        total = total + i.quantity * i.price
    return render(request, 'bill.html', {'bill': bill, 'total': total})


def place(request):
    username = request.session['username']
    op = Order.objects.filter(user_id=username)
    product=Product.objects.all()
    for i in op:
        i.delete()
    return render(request, 'eshop.html', {'msg1': 'Your Order Placed Successfully! ','product':product})


def add(request):
    try:
        username = request.session['username']
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        if int(quantity) < 1:
            return render(request, 'eshop.html', {'msg': 'Cannot add to cart'})

        qu = Product.objects.get(id=item)
        price = qu.price
        for i in Order.objects.all():
            if i.p_id == qu and username == i.user_id:
                i.quantity = int(i.quantity) + int(quantity)
                i.save()
                return HttpResponseRedirect('/cart/')
        q = Order(
            user_id=username,
            o_date=datetime.datetime.now(),
            price=price,
            p_id=qu,
            quantity=quantity,
            images=qu.img,
            item=qu.product_name,
        )
        qu=Ordered(
            user_id=username,
            o_date=datetime.datetime.now(),
            price=price,
            p_id=qu,
            quantity=quantity,
            images=qu.img,
            item=qu.product_name,
        )
        q.save()
        qu.save()
        u=request.session['username']
        print(u)
        return HttpResponseRedirect('/cart/')
    except KeyError:
        return render(request, 'login.html', {'msg': 'Please Login to Modify your Cart!'})
    except ValueError:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request):
    username = request.session['username']
    item = request.POST.get('item')
    qu = Product.objects.get(id=item)
    for o in Ordered.objects.all():
        if o.p_id == qu and username == o.user_id:
            o.delete()


    for i in Order.objects.all():
        if i.p_id == qu and username == i.user_id:
            i.delete()
            return HttpResponseRedirect('/cart/')
    return HttpResponseRedirect('/cart/')