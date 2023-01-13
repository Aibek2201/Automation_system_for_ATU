from django.contrib import admin
from main.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'photo', 'time_create')




admin.site.register(User, UserAdmin)