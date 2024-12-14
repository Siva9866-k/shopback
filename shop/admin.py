from django.contrib import admin
from django.utils.html import format_html  # Added this import for format_html
from .models.product import Product, Offers, ProductCategory  # Ensure ProductCategory is imported
from .models.category import Category
from .models.customer import Customer
from .models.cart import CartItem

# Register ProductCategory with preview
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_image_preview']
    
    def category_image_preview(self, obj):
        if obj.cat_img:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.cat_img.url)
        return "-"
    category_image_preview.short_description = "Image"

# Register your models here
class Categoryinfo(admin.ModelAdmin):
    list_display = ["name", "cat_img"]

class Productinfo(admin.ModelAdmin):
    list_display = ["name", "category", "price"]

class Customerinfo(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "mobile"]

class Offersinfo(admin.ModelAdmin):
    list_display = ["title", "offer_name", "offer_img", "offer"]

class Cartinfo(admin.ModelAdmin):
    list_display = ["user", "product", "quantity"]

admin.site.register(Product, Productinfo)
admin.site.register(Offers, Offersinfo)
admin.site.register(Category, Categoryinfo)
admin.site.register(Customer, Customerinfo)
admin.site.register(CartItem, Cartinfo)
