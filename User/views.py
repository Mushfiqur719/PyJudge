from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .form import UserRegistrationForm, UserDetailsForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user, authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        dict = request.POST
        error_fname = ''
        if dict['fname']!='':
            print(dict['fname'])
        else:
            error_fname = 'First name is required*'
            return  render(request, 'user/profile.html', {'form': form,'error_fname':error_fname})
        if dict['lname']!='':
            print(dict['lname'])
        else:
            error_lname = 'Second name is required*'
            return  render(request, 'user/profile.html', {'form': form,'error_lname':error_lname})
        if dict['gender']!='':
            print(dict['gender'])
        else:
            error_gender = 'Gender is required*'
            return  render(request, 'user/profile.html', {'form': form,'error_gender':error_gender})
        if 'vehicle1' in dict:
            print(dict['vehicle1'])
        if 'vehicle1' in dict:
            print(dict['vehicle2'])
        if 'vehicle1' in dict:
            print(dict['vehicle3'])

        return redirect('home')
    else:
        form = UserDetailsForm()
    
    return render(request, 'user/profile.html', {'form': form})


def register(request):
    if(request.method == "POST"):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            # error = ''
            # dict = request.POST
            # email = dict['email']
            # check = User.objects.get(email='email')
            # if check == None:
            #     form.save()
            # else:
            #     error = 'Email alreadey exists'

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            new_user = authenticate(username=username,password=password)
            login(request,new_user)

            message = 'Welcome to PyJudge '+username
            # message.success(request,message=message)

            return redirect('home')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'User/register.html', {'form': form})