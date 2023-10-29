from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render  # Import your form

from foods.models import Food
from orders.forms import FoodOrderingForm


@login_required
def order_food(request):

    if request.method == 'POST':
        form = FoodOrderingForm(request.POST or None)

        if form.is_valid():
            orders = form.save(commit=False)  # Create a reservation object without saving
            orders.user = request.user  # Associate the reservation with the logged-in user

            orders.save()  # Now save to the database

            return HttpResponse("Order Confirmed")
    else:
        form = FoodOrderingForm(request.POST or None)

    return render(request, 'form2.html', {'form2': form})
