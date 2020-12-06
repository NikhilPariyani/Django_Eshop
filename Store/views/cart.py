from django.shortcuts import render, redirect
from django.http import HttpResponse
from Store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from Store.models.product import Product

# Cart Class
class Cart(View):

    def get(self,request):
        empty = None
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        if not products:
            empty = 1
        print(products)
        return render(request, 'cart.html' , {'products' : products, 'empty' : empty})
