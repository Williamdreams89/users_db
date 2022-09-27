from django.contrib import admin

from base.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', "email", "department", "role"]

admin.site.register(User, UserAdmin)
