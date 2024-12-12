from django.contrib import admin
from .models.product import Product,Offers
from .models.category import Category
from .models.customer import Customer
from .models.cart import CartItem
#from .models import Product, Category, Customer,Offers


# Register your models here.
class Categoryinfo(admin.ModelAdmin):
    list_display=["name","cat_img"]
class Productinfo(admin.ModelAdmin):
    list_display=["name","category","price"]
class Customerinfo(admin.ModelAdmin):
    list_display=["first_name","last_name","email","mobile"]
class Offersinfo(admin.ModelAdmin):
    list_display=["title","offer_name","offer_img","offer"] 
class Cartinfo(admin.ModelAdmin):
    list_display=["user","product","quantity"]              
admin.site.register(Product,Productinfo)
admin.site.register(Offers, Offersinfo)
admin.site.register(Category,Categoryinfo)
admin.site.register(Customer,Customerinfo)
admin.site.register(CartItem,Cartinfo)