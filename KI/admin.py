from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['tytul', 'autor', 'rok', 'kategoria', 'opis', 'zdjecie']
    search_fields =['autor', 'tytul', 'kategoria']