from django.http import HttpResponse
from django.shortcuts import render
from .models import Pizza


def index(request):
    pizzas = Pizza.objects.all()
    return render(request, 'index.html',
                  {'pizzas': pizzas})


def new(request):
    return HttpResponse('New Products')

