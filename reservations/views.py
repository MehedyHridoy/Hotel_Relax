from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .forms import TableReservationForm  # Import your form

@login_required
def reserve_table(request):
    if request.method == 'POST':
        form = TableReservationForm(request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)  # Create a reservation object without saving
            reservation.user = request.user  # Associate the reservation with the logged-in user
            reservation.save()  # Now save to the database

            return HttpResponse("Table Reserved Successfully")
    else:
        form = TableReservationForm()

    return render(request, 'form.html', {'form': form})
