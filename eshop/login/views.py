from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Customer


# Create your views here.


def login(request):
    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'signup.html', {})


def createUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        email = request.POST['email']
        address = request.POST['address']
        gender = request.POST['gender']
        mobile_no = request.POST['mno']
        cimg = request.FILES.get('cimg',"p.jpg")
        if password == repassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'UserName Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                cust = Customer(customer_name=username, password=password, email=email, gender=gender,
                                mobile_no=mobile_no, address=address, cimg=cimg)
                cust.save()
                messages.info(request, 'User created')
                return redirect('/login')
        else:
            messages.info(request, 'Password is not matching....')
            return redirect('signup')
    else:
        return render(request, 'signup.html', {})


def loginAuth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = auth.authenticate(username=username, password=password)
        if username=='admin@123':
            if password=='!@#admin!@#':
                auth.login(request,user)
                request.session['username'] = username
                return redirect('/owner')
        print(user)
        if user is not None:
            auth.login(request, user)
            request.session['username'] = username
            user_id = request.session['username']
            print(user_id)
            return redirect('/')
        else:
            messages.info(request, 'invalid username or password...')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout(request):
   # del request.session['username']
    auth.logout(request)
    messages.info(request, 'YOU ARE LOGGED OUT')
    return redirect('/')

