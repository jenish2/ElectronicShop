from django.urls import path
from .views import add,pay,bill,remove,place,cart
from login.views import loginAuth,signup,createUser
urlpatterns=[
    
    path('add/',add,name="add"),
    path('payment/',pay,name="pay"),
    path('bill/',bill,name="bill"),
    path('remove/',remove,name="remove"),
    path('place/',place,name="place"),
    path('',cart,name="cart"),
    path('add/loginAuth',loginAuth,name="loginAuth"),
    path('add/signup',signup,name="signup"),  
    path('add/createUser',createUser,name="createUser"),
]