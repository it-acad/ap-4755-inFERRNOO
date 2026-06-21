from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff_user')
    
    list_filter = ('role', 'is_active')
    
    search_fields = ('email', 'first_name', 'last_name')
    
    fieldsets = (
        ('Особисті дані', {
            'fields': ('email', 'first_name', 'middle_name', 'last_name')
        }),
        ('Налаштування доступу', {
            'fields': ('role', 'is_active'),
            'classes': ('wide',),
        }),
    )

    def is_staff_user(self, obj):
        return obj.is_staff
    is_staff_user.boolean = True
    is_staff_user.short_description = 'Is Staff'