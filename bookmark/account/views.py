from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm, UserRegistrationForm


def user_login(request):
    template_name = 'account/login.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully.')
                else:
                    return HttpResponse('Disabled account.')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, template_name, context=context)

def register(request):
    template_name = 'account/register.html'
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])   # hashing
            # Save the User object
            new_user.save()
            return render(request, 'account/register-done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, template_name, {'user_form': user_form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
