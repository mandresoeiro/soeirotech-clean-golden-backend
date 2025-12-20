from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ('email',)
    list_display = ('id', 'email', 'full_name', 'is_active', 'is_verified')
    search_fields = ('email', 'full_name')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('full_name',)}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_verified')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )

    filter_horizontal = ()
