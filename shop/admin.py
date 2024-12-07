from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models import Product, Category, Customer


# Register your models here.
class Categoryinfo(admin.ModelAdmin):
    list_display=["name"]
class Productinfo(admin.ModelAdmin):
    list_display=["name","category","price"]
class Customerinfo(admin.ModelAdmin):
    list_display=["first_name","last_name","email","mobile"]      
admin.site.register(Product,Productinfo)
admin.site.register(Category,Categoryinfo)
admin.site.register(Customer,Customerinfo)