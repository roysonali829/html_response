"""
URL configuration for project14 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new1/',new1,name='new1'),
    path('new2/',new2,name='new2'),
    path('new3/',new3,name='new3'),
    path('new4/',new4,name='new4'),
    path('new5/',new5,name='new5'),
    path('new6/',new6,name='new6'),
    path('new7/',new7,name='new7'),
    path('new8/',new8,name='new8'),
    path('new9/',new9,name='new9'),
    path('new10/',new10,name='new10'),
    path('new11/',new11,name='new11'),
    path('new12/',new12,name='new12'),
    path('new13/',new13,name='new13'),
    path('new14/',new14,name='new14'),
    path('new15/',new15,name='new15'),
]
