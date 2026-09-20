from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404

from actions.models import Action
from actions.utils import create_action
from .forms import (
    LoginForm,
    UserRegistrationForm,
    UserEditForm,
    ProfileEditForm,
)
from .models import Profile, Contact


User = get_user_model()


@login_required
def user_list(request):
    template_name = 'account/user/list.html'
    users = User.objects.filter(is_active=True)
    context = {
        'users': users,
        'section': 'people',
    }
    return render(request, template_name, context=context)


@login_required
def user_detail(request, username):
    template_name = 'account/user/detail.html'
    user = get_object_or_404(User, username=username, is_active=True)
    context = {
        'user': user,
        'section': 'people',
    }
    return render(request, template_name, context=context)


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
            # Create the user Profile
            Profile.objects.create(user=new_user)
            create_action(new_user, 'has created an account')
            return render(request, 'account/register-done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, template_name, {'user_form': user_form})


@login_required
def dashboard(request):
    template_name = 'account/dashboard.html'
    # Display all actions by default
    actions = Action.objects.exclude(user=request.user)
    following_ids = request.user.following.values_list('id', flat=True)
    if following_ids:
        # If user is followig others, retrieve oly their actions
        actions = actions.filter(user_id__in=following_ids)
    actions = actions.select_related('user', 'user__profile').prefetch_related('target')[:10]

    context = {
        'actions': actions,
        'section': 'dashboard',
    }
    return render(request, template_name, context=context)


@login_required
def edit(request):
    template_name = 'account/edit.html'

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updatign your profile')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)


    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, template_name, context=context)


@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')

    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user, user_to=user)
                create_action(request.user, 'is following', user)
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
            return JsonResponse({'status': 'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error'})
    return JsonResponse({'status': 'error'})
