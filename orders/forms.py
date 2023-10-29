from django import forms

from orders.models import Order


class FoodOrderingForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'foods',
            'quantity',
        ]
