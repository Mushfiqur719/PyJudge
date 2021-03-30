from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from . form import UserRegistrationForm


def profile(request):
    context = {
        'name': "Mushfiqur",
        'email': "rahmanmushfiqur719@gmail.com",
        'problem_solved': ['309', '310', '405', '210']
    }
    return render(request, 'user/profile.html', context)


def register(request):
    if(request == "post"):
        form = UserRegistrationForm(request.post)
        if form.is_valid():
            form.save()
    else:
        form = UserRegistrationForm()
        return render(request, 'user/register.html', {'form': form})
