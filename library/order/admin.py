from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'created_at', 'plated_end_at', 'end_at', 'is_returned')
    
    list_filter = ('created_at', 'end_at', 'plated_end_at')
    
    search_fields = ('user__first_name', 'user__last_name', 'book__name')

    fieldsets = (
        ('Основна інформація (Незмінні дані)', {
            'fields': ('user', 'book', 'created_at')
        }),
        ('Терміни та статус (Змінні дані)', {
            'fields': ('plated_end_at', 'end_at')
        }),
    )

    readonly_fields = ('created_at',)

    def is_returned(self, obj):
        return obj.end_at is not None
    is_returned.boolean = True
    is_returned.short_description = 'Повернуто'