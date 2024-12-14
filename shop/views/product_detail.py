from django.shortcuts import render, get_object_or_404
from ..models.product import Product

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    products = Product.objects.all()
    #thumbnails = [product.thumbnail1, product.thumbnail2, product.thumbnail3]
    return render(request, 'product_detail.html', {'product': product, 'products': products,})

