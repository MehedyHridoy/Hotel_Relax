from django.contrib.auth.models import User
from django.db import models

from foods.models import Food


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foods = models.ManyToManyField(Food)
    quantity = models.IntegerField()

    # def __str__(self):
    #     return self.user.username + '->' + self.foods.name

