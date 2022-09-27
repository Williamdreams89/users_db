from django.contrib import admin

from base.models import Student, User

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', "email", "department", "role"]

admin.site.register(User, UserAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display  = ["name", "email", ]

admin.site.register(Student, StudentAdmin)