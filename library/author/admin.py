from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'patronymic')
    
    search_fields = ('surname', 'name')
    
    list_filter = ('surname',)

    fieldsets = (
        ('Персональні дані', {
            'fields': ('name', 'surname', 'patronymic')
        }),
    )