from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from orders_new import forms

def order_new(request):
    if request.method == 'POST':
        order_form = forms.OrderNewForm(request.POST or None)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.save()

            return HttpResponse('Order placed!')

    else:
        order_form = forms.OrderNewForm(request.POST or None)
    return render(request, 'order_form.html', {

        'order_form': order_form
    })

