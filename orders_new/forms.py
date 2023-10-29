from django import forms

from orders_new.models import Order_New


class OrderNewForm(forms.ModelForm):
    class Meta:
        model = Order_New
        fields = [
            'foods',
            'description',
        ]