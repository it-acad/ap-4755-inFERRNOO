from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'count', 'get_authors', 'borrower')
    
    list_filter = ('authors', 'borrower')
    
    search_fields = ('id', 'name', 'authors__name')

    fieldsets = (
        ('Основна інформація (Статичні дані)', {
            'fields': ('name', 'description', 'authors')
        }),
        ('Дані про видачу (Змінні дані)', {
            'fields': ('count', 'borrower'),
            'classes': ('collapse',), 
        }),
    )

    def get_authors(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])
    get_authors.short_description = 'Authors'

    filter_horizontal = ('authors',)