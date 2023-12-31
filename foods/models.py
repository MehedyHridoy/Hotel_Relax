from django.db import models


# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()

    def __str__(self):
        return 'Food Name: ' + self.name
