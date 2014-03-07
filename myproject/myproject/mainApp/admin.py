from django.contrib import admin

# Register your models here.

from myproject.mainApp.models import Plan,User

admin.site.register(Plan)
admin.site.register(User)