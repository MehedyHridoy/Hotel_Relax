from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *


# Create your views here.

@login_required
def profile(request):  # Main screen
    return render(request, template_name='registration/profile.html', context={'section': 'profile'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the user object
            new_user.save()
            return render(request, template_name='registration/register_done.html', context={'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', context={'user_form': user_form})
