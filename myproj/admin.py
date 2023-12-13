from django.contrib import admin
from myproj.models import members
from myproj.models import employee
from myproj.models import adminlogin

admin.site.register(members)
admin.site.register(employee)
admin.site.register(adminlogin)