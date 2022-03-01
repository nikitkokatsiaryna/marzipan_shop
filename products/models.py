from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    product_image = models.ImageField(null=True, blank=True, default="img/logo2.png")
    price = models.FloatField()
    ingredients = models.TextField()
