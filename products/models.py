from django.db import models


class Pizza(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')


class CartItem(models.Model):
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
	qty = models.PositiveIntegerField(default=1)
	item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)


class Cart(models.Model):
	items = models.ManyToManyField(CartItem, blank=True)
	cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
