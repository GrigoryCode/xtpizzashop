from django.db import models


class Pizza(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')

