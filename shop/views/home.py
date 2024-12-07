from django.shortcuts import render
from django.http import HttpResponse
from shop.models.product import Product
from shop.models.category import Category
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from shop.models.customer import Customer
from django.views import View  # Correct import for class-based views

class home(View):
    def get(self, request):
        categories = Category.objects.all()
        category_id = request.GET.get('category')

        if category_id:
            products = Product.get_category_id(category_id)
        else:
            products = Product.objects.all()

        data = {'products': products, 'categories': categories}
        return render(request, 'index.html', data)

'''
#class based view
class home(View):
    def get(self,request):
        categories=Category.objects.all()
        categoryId=request.GET.get('category')
        if categoryId:
           products=Product.get_category_id(categoryId)
        else:
        products=Product.objects.all()   
        data={'products':products,'categories':categories}
         return render(request,'index.html',data)
    #def post(self,request):'''
           