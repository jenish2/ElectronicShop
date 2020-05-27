from django.urls import path
from .views import login,signup,createUser,loginAuth,logout

urlpatterns = [
    path('',login,name='login'),
    path('signup',signup,name='signup'),
    path('createUser',createUser,name='createUser'),
    path('logout',logout,name='logout'),
    path('loginAuth',loginAuth,name='loginAuth'),
   
]