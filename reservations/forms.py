from django import forms

from reservations.models import Reservation


class TableReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'reservation_datetime',
            'guests',
            'special_requests',
        ]
