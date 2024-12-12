from django.urls import path
from .views.cart import cart_view
from .views.home import home
from .views.signup import signup
from .views.login import login

urlpatterns = [
    # Home, Signup, Login Views
    path('', home.as_view(), name='home'),
    path('signup', signup.as_view(), name='signup'),
    path('login', login.as_view(), name='login'),

    # Cart Views
    path('cart/', cart_view, name='cart'),  # Unified cart view for displaying the cart and handling actions
]




'''from django.urls import path
from .views.home import home
from .views.signup import signup
from .views.login import login #filename import class
from . import views

urlpatterns = [
    path('', home.as_view(), name='home'),          # Add a name for the home view
    path('signup', signup.as_view(), name='signup'),  # Add a name for the signup view
    path('login', login.as_view(), name='login'),    # Add a name for the login view
]'''

