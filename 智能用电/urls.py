"""智能用电 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from SE import views
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('dianya/',views.dianya,name='dianya'),
    path('dianliu/',views.dianliu,name='dianliu'),
    path('gonglv/',views.gonglv,name='gonglv'),
    path('dianliang/',views.dianliang,name='dianliang'),
    path('recv_data/',views.recv_data),
    path('login/',views.login,name = 'login'),
    path('create_account/',views.create_account,name='create_account'),
]
