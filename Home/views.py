from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user, authenticate, login

# @login_required
def home(request):
    return render(request, 'user/home.html',)
