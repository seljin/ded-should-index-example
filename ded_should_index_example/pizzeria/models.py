from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=64)


class Pizza(models.Model):
    name = models.CharField(max_length=64)
    toppings = models.ManyToManyField(Topping)
