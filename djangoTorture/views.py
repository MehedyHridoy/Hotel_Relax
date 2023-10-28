from django.shortcuts import render

from foods.models import Food


def home(request):
    return render(request, 'home.html')


def menu(request):
    return render(request, 'menu.html')
def order(request):
    foods = Food.objects.all()
    return render(request, 'order.html', {
        "foods": foods
    })
def reservation(request):
    return render(request, 'reservation.html' )
def contract(request):
    return render(request, 'contract.html' )