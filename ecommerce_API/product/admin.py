from django.contrib import admin
from .models import Category, Brand, ProductImage, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description' , 'category' , 'brand' , 'quantity' , 'price' ,'date_added' , 'product_image')
    search_fields = ('name', 'price', 'description' , 'category' , 'brand' , 'quantity' , 'price' ,'date_added' )
    # list_per_page = 20
    ...
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

# Register your models here.
admin.site.register(Category , CategoryAdmin)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
