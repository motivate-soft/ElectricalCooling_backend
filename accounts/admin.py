from django.contrib import admin
from accounts.models import CustomUser


class UserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['id', 'email', 'first_name', 'last_name', 'last_login', 'is_superuser', 'is_staff', 'is_active']


admin.site.register(CustomUser, UserAdmin)
