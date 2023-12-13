import sys
import os
from . import views
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