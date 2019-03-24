from django.db import models


class Pizza(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.FloatField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.TextField(max_length=300)
    discount = models.FloatField()
