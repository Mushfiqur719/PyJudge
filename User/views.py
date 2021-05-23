from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user, authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.views import generic
from django.urls import reverse_lazy





@login_required
def home(request):
    return render(request, 'user/home.html',)

def register(request):
    if(request.method == 'POST'):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
<<<<<<< HEAD
            messages.success(request, f"Your account has been created!")

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            new_user = authenticate(username=username, password=password)
            login(request, new_user)

            subject = 'Pyjudge Registration Successful'
            body = render_to_string('intro_mail.html')

            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [new_user.email]
            )
=======
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!')
>>>>>>> b8c18d301da0bf66dc8a40a11809e789f62d6b2e
            return redirect('home')
        else:
            return render(request, 'User/register.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'User/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'user/profile.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your account has been updated')
            return redirect('profile')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form,
    }
    return render(request, 'user/profile_update.html',context)


