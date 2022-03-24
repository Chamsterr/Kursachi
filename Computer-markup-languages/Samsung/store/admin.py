from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Product, Category

from django.utils.safestring import mark_safe


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', 'preview')
    list_display_links = ('name', 'description')
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height=100px >')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)