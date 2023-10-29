from django.urls import path
from . import views

urlpatterns = [
    path('order-form/', views.order_new, name='order-form'),
]
