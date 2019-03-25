from django.contrib import admin
from .models import Pizza, CartItem, Cart


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(CartItem)
admin.site.register(Cart)
