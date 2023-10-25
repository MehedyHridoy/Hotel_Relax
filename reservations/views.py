# # Create your views here.
# from django.contrib.auth.models import User
# from django.http import HttpResponse
# from django.shortcuts import render
# from . import forms
#
#
# def reserve_table(request):
#     if request.method == 'GET':
#
#         form = forms.TableReservationForm(request.GET)
#
#         if form.is_valid():
#             form.save()
#
#             return HttpResponse("Table Reserved Successfully")
#
#     else:
#         form = forms.TableReservationForm()
#
#     return render(request, 'form.html', {
#         'form': form
#     })
#


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
