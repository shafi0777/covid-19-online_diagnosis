from django.contrib import admin

# Register your models here.

from  django.contrib.auth.models import User

from CovidiaV02.models import CovidiaAppUser

class WebAppUserAdmin(admin.ModelAdmin):
    list_display = ['username','email','is_admin']


admin.site.register(CovidiaAppUser, WebAppUserAdmin)
