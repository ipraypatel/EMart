from django.shortcuts import render
from django.views import View
from Store.models.order import Order

class OrderView(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        customer = request.session.get('customer')
        order = Order.get_orders_by_customer(customer)
        return render(request, 'order.html', {'order': order})