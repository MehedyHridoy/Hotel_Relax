from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from reviews import forms


# Create your views here.

def review(request, id):
    user = User.objects.get(pk=id)

    if request.method=='POST':
        rev_form = forms.ReviewForm(request.POST or None)

        if rev_form.is_valid():
            rev = rev_form.save(commit=False)
            rev.user = request.user
            rev.save()

            return redirect('/')

    else:
        rev_form = forms.ReviewForm(request.POST or None)
    return render(request, 'review_form.html',{
        'user':user,
        'rev_form':rev_form
    })