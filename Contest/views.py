from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Tutorials
#from django.contrib.auth import get_user, authenticate, login

@login_required
def contest(request):
    return render(request, 'Contest/contest.html')

class TutorialView(ListView):
    model = Tutorials
    template_name = 'Contest/tutorials.html'

# @login_required
# def tutorials(request):
#     return render(request, 'Contest/tutorials.html')
