from django.shortcuts import render, get_object_or_404
from shop.models.product import Product
from django.shortcuts import render, redirect  # Import redirect here
from django.http import JsonResponse
from shop.models.cart import CartItem # Adjust this according to your models


def cart_view(request):
    """Unified view to handle all cart actions using session-based cart."""
    session_cart = request.session.get('cart', {})  # Retrieve cart from session
    cart_items = []

    # Fetch products in the cart
    for product_id, quantity in session_cart.items():
        product = get_object_or_404(Product, id=product_id)
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': product.price * quantity,
        })

    # Handle 'add to cart' action
    if request.method == "POST" and 'add_to_cart' in request.POST:
        product_id = str(request.POST.get('product_id'))
        session_cart[product_id] = session_cart.get(product_id, 0) + 1
        request.session['cart'] = session_cart  # Save back to session
        return redirect('cart')

    # Handle 'remove from cart' action
    if request.method == "POST" and 'remove_from_cart' in request.POST:
        product_id = str(request.POST.get('product_id'))
        if product_id in session_cart:
            del session_cart[product_id]
            request.session['cart'] = session_cart
        return redirect('cart')

    # Handle 'update quantity' action
    if request.method == "POST" and 'update_quantity' in request.POST:
        product_id = str(request.POST.get('product_id'))
        action = request.POST.get('action')  # 'increase' or 'decrease'
        if product_id in session_cart:
            if action == "increase":
                session_cart[product_id] += 1
            elif action == "decrease" and session_cart[product_id] > 1:
                session_cart[product_id] -= 1
            request.session['cart'] = session_cart
        return redirect('cart')

    # Calculate total amount
    total_amount = sum(item['total_price'] for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_amount': total_amount,
    }
    return render(request, 'cart.html', context)
