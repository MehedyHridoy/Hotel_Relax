from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def menu(request):
    return render(request, 'menu.html')
def order(request):
    return render(request, 'order.html' )
def reservation(request):
    return render(request, 'reservation.html' )
def contract(request):
    return render(request, 'contract.html' )