"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Branch.views import Branch
from List.views import List
from home.views import index
from home.views import login
from home.views import register
from Branch.views import add_branch
from List.views import add_list




urlpatterns = [
    path('admin/', admin.site.urls),
    path('Branch/',Branch,name='Branch'),
    path('List/',List,name='List'),
    path('index/',index),
    path('login/',login),
    path('',register),
    path('add_branch/',add_branch,name='add_branch'),
    path('add_list/',add_list,name='add_list'),]   
