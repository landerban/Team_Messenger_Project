from django.contrib import admin
from django.contrib.auth.models import UserManager
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'user_id', 'first_name',
                    'last_name', 'is_staff', 'is_active')
    search_fields = ('email', 'user_id', 'first_name', 'last_name')
    ordering = ('email',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if not request.user.is_superuser:
            fieldsets = [f for f in fieldsets if f[0] != 'Permissions']
        return fieldsets
