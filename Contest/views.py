from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import get_user, authenticate, login


def contest(request):
    return render(request, 'Contest/contest.html')

def tutorials(request):
    return render(request, 'Contest/tutorials.html')
