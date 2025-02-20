from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile

# Customizing the UserAdmin
class CustomUserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'role', 'is_admin', 'is_staff')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    list_filter = ('role', 'is_admin', 'is_staff', 'is_active')
    ordering = ('-date_joined',)
    
    fieldsets = (
        ('Personal Information', {'fields': ('first_name', 'last_name', 'username', 'email', 'phone_number', 'role')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'role', 'is_admin', 'is_staff', 'is_active'),
        }),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
