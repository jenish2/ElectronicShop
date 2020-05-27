from django.urls import path
from login.views import logout
from .views import shop,laptop,mobile,tv,contactus,aboutus,productview,checkout,profile
urlpatterns = [
    path('',shop,name='shop'),
    path('laptop',laptop,name='laptop'),
    path('mobile',mobile,name='mobile'),
    path('tv',tv,name='tv'), 
    path('contactus',contactus,name='contactus'), 
    path('aboutus',aboutus,name='abouttus'),
    path('productview/<int:myid>',productview,name='productview'),
    path('checkout',checkout,name='checkout'),
    path('profile',profile,name="profile"),
]