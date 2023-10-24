from django.db import models
from django.contrib.auth.models import User
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    reservation_datetime = models.DateTimeField()
    guests = models.CharField(default='2',max_length=20)
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reservation for {self.guests} at {self.reservation_datetime}"
