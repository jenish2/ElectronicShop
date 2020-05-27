from django.urls import path
from .views import showQuery,showOrder,showUser,owner,addProduct,add,removeProduct,remove
urlpatterns = [
    path('',owner,name="owner"),
    path('showQuery',showQuery,name="showQuery"),
    path('showOrder',showOrder,name="showOrder"),
    path('showUser',showUser,name="showUser"),
    path('addProduct',addProduct,name="addProduct"),
    path('add',add,name="add"),
    path('removeProduct',removeProduct,name="removeProduct"),
    path('remove/<int:myid>',remove,name="remove"),
]
