from django.contrib.auth.models import User
from django.db import models

from foods.models import Food


# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    foods = models.ForeignKey(Food, on_delete=models.CASCADE, default=None)
    rating = models.IntegerField()
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.user.username + '->' + self.foods.name


