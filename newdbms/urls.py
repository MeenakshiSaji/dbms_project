"""
URL configuration for newdbms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import sys
import os
from myproj import views
from django.contrib import admin
from django.urls import path
from myproj.views import trainer_login,trainer_success,trainer_reset_password_page,reset_password

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

urlpatterns=[
    path('admin/',admin.site.urls),
    path('trainer_login/',views.trainer_login,name='trainer_login'),
    path('esuccess/<int:user_id>/',views.trainer_success,name='trainer_success'),
    path('trainer_reset_password/<int:user_id>/',views.trainer_reset_password_page,name='trainer_reset_password_page'),
    path('reset_password/<int:user_id>/',views.reset_password,name='reset_password')
]