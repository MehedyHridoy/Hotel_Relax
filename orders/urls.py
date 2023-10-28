from django.urls import path
from . import views

urlpatterns = [
    path('order-food/', views.order_food, name='order-food')
]