"""Dmart_Application URL Configuration

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
from django.urls import path

from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from Dmart_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='registration'),
    path('login/', views.login, name='login'),
    path('login/registration.html', views.login, name='login'),
    path('booking/', views.booking, name='booking'),
    path('display/', views.display, name='display'),
    path('multiply/', views.multiply,name='multiply'),
    path('Dmart_App/display/',views.display,name='display'),
    path('Dmart_App/',views.booking,name='booking'),
    path('Dmart_App/display/multiply', views.multiply,name='multiply'),
]