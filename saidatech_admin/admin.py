from django.contrib import admin
from .models import saidatech_admin_profile

# Register your models here.


class saidatech_adminAdmin(admin.ModelAdmin):

    list_display=('saidatech_admin_id','fname','lname', 'email', 'phone')
     
admin.site.register(saidatech_admin_profile, saidatech_adminAdmin)

