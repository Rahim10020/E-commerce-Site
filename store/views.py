from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, ShippingAddress, Customer, Order, OrderItem


# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {
        'items': items,
        'order': order
    }
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {
        'items': items,
        'order': order
    }
    return render(request, 'store/checkout.html', context)

def update_item(request):
    return JsonResponse("Item added sucessfully", safe=False)
