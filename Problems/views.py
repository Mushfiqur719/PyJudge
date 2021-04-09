from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Problems
from .forms import ProblemForm

#from django.contrib.auth import get_user, authenticate, login

@login_required
def problems(request):
    problems = Problems.objects.all()
    context = {
        'problems' : problems,
    }
    return render(request, 'Problems/problems.html', context)

@login_required
def categories(request):
    return render(request, 'Problems/categories.html')

@login_required
def add_problems(request):
    problems = Problems.objects.all()
    if request.method == 'POST':
        form = ProblemForm(request.POST)
    else:
        form = ProblemForm()
    context = {
        'problems' : problems,
        'form' : form,
    }
    return render(request, 'Problems/add_problems.html', context)

