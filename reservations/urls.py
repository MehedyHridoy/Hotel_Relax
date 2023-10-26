from django.urls import path
from . import views

urlpatterns = [
    path('reserve_table/', views.reserve_table, name='reserve-table')
]
