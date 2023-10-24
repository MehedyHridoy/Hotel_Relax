# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .import forms


def reserve_table(request):

    if request.method == 'GET':

        form = forms.TableReservationForm(request.GET)

        if form.is_valid():
            form.save()

            return HttpResponse("Table Reserved Successfully")

    else:
        form = forms.TableReservationForm()

    return render(request, 'form.html', {
        'form':form
    })