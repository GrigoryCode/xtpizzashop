from django.http import HttpResponse
from django.shortcuts import render
from .models import Pizza, CartItem, Cart


def index(request):
    cart = Cart.objects.first()
    pizzas = Pizza.objects.all()[0:4]
    return render(request, 'index.html',
                  {'pizzas': pizzas, 'cart': cart})


def new(request):
    return HttpResponse('New Products')


def cart(request):
    cart = Cart.objects.first()
    context = {
        'cart': cart
    }
    return render(request, 'cart.html', context)
