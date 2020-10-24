from django.urls import path
from .views import Index, Signup, Login, logout, Cart, CheckOut, OrderView
from Store.middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name="homepage"),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('order', auth_middleware(OrderView.as_view()), name='order')
]