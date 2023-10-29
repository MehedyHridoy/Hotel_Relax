from django.urls import path
from . import views

urlpatterns = [
    path('review/<int:id>', views.review, name='review-form'),
]
