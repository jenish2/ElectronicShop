"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from login import urls as LoginUrl
from shop import urls as pshop
from cart import urls as pcart
from login import views
from owner import urls as powner
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('owner/',include(powner)),
    path('cart/',include(pcart)),
    path('login/',include(LoginUrl)),
    path('admin/', admin.site.urls),
    path('',include(pshop)),
    

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
