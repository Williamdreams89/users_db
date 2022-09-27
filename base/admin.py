from django.contrib import admin

from base.models import User

class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User
        fields = "__all__"

        