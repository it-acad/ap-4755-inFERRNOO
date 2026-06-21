from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'created_at', 'is_returned')
    
    list_filter = ('user', 'created_at', 'end_at')
    
    search_fields = ('user__email', 'book__name')
    
    fieldsets = (
        ('Статичні дані', {
            'fields': ('user', 'book', 'created_at', 'plated_end_at')
        }),
        ('Змінні дані', {
            'fields': ('end_at',),
        }),
    )

    readonly_fields = ('created_at',)

    def is_returned(self, obj):
        return obj.end_at is not None
    is_returned.boolean = True
    is_returned.short_description = 'Повернуто'

    def get_readonly_fields(self, request, obj=None):
        if obj:  
            return ('user', 'book', 'created_at', 'plated_end_at')
        return ('created_at',) 