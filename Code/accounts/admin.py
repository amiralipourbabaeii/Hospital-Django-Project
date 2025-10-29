# accounts/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import RegisterForm

User = get_user_model()

if admin.site.is_registered(User):
    admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    add_form = RegisterForm
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )