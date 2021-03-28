from django.shortcuts import render, redirect
from .form import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm



def profile(request):
    context = {
        'name': "Mushfiqur",
        'email': "rahmanmushfiqur719@gmail.com",
        'problem_solved': ['309', '310', '405', '210']
    }
    return render(request, 'user/profile.html', context)


def register(request):
    if(request == "POST"):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
        return render(request, 'User/register.html',{'form':form})