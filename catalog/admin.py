from django.contrib import admin
from catalog.models import Category, Product


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description'
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'price',
        'category'
    ]
    list_filter = ['category']
    ordering = ['name']
    search_fields = ['name', 'description']

