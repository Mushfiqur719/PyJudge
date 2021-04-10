from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Problems
from .forms import ProblemForm
from django.views.generic import ListView, DetailView
import sys

#from django.contrib.auth import get_user, authenticate, login

class ProblemView(ListView):
    model = Problems
    template_name = 'Problems/problems.html'

class ProblemDetailView(DetailView):
    model = Problems
    template_name = 'Problems/solve.html'

@login_required
def home(request):
    return render(request, 'user/home.html',)


# @login_required
# def problems(request):
#     problems = Problems.objects.all()
#     # categories = Problems.objects.filter()
#     context = {
#         'problems' : problems,
#     }
#     return render(request, 'Problems/problems.html', context)

@login_required
def categories(request):
    return render(request, 'Problems/categories.html')

@login_required
def add_problems(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('problems')
    else:
        form = ProblemForm()
    context = {
        'form' : form,
    }
    return render(request, 'Problems/add_problems.html', context)

@login_required
def delete_problems(request):
    return render(request, 'Problems/problems.html')

@login_required
def solve(request):
    return render(request, 'Problems/solve.html')
    
@login_required
def runcode(request):
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = request.POST['input_area']
        y = input_part
        input_part = input_part.replace("\n"," ").split(" ")
        def input():
            a = input_part[0]
            del input_part[0]
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        print(output)
    res = render(request,'Problems/solve.html',{"code":code_part,"input":y,"output":output})
    return res


