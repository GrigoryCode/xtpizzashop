from django.contrib import admin
from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')


admin.site.register(Pizza, PizzaAdmin)
