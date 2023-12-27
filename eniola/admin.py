from django.contrib import admin
from .models import UserFormGrabber

# Register your models here.


class UserFormGrabberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'country')
    list_display_links = ('firstname', 'lastname', 'email', 'phone', 'country')
   


admin.site.register(UserFormGrabber, UserFormGrabberAdmin)