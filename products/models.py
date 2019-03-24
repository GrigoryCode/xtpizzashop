from django.db import models

class Pizza(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    image_url = models.CharField()
