from django.shortcuts import render, redirect
from django.http import HttpResponse
from Store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from Store.models.product import Product
from Store.models.orders import Order
from Store.middlewares.auth import auth_middleware
#from django.utils.decorators import method_decorator

# Orders Class
class OrderView(View):

   # @method_decorator(auth_middleware)
    def get(self,request):
       customer = request.session.get('customer')
       orders = Order.get_orders_by_customer(customer)
       print(orders)
       return render(request, 'orders.html', {'orders' : orders})