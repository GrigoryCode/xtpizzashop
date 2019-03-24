from django.contrib import admin
from .models import Pizza, Offer


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Offer, OfferAdmin)