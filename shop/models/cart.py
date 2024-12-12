from django.db import models
from django.shortcuts import redirect
from django.shortcuts import render, redirect  # Import redirect here
from django.http import JsonResponse
from .product import Product  # Adjust this according to your models

from django.contrib.auth.models import User
from .product import Product  # Import the Product model

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link the cart item to a user
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link the cart item to a product
    quantity = models.PositiveIntegerField(default=1)  # Store product quantity
    saved_for_later = models.BooleanField(default=False)  # Allow "Save for Later" functionality

    def item_total(self):
        """Calculate the total price for this cart item."""
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

