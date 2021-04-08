from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import get_user, authenticate, login

@login_required
def contest(request):
    return render(request, 'Contest/contest.html')

@login_required
def tutorials(request):
    return render(request, 'Contest/tutorials.html')
