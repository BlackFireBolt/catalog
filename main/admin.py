from django.contrib import admin

from .models import SuperCategory, SubCategory, Product
from .forms import SubCategoryForm


class SubCategoryInline(admin.TabularInline):
    model = SubCategory


class SuperCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    exclude = ('super_category', )
    inlines = (SubCategoryInline, )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(SuperCategory, SuperCategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    form = SubCategoryForm


admin.site.register(SubCategory, SubCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
