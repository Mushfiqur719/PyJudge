from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Problems
from .forms import ProblemForm
from django.views.generic import ListView, DetailView, CreateView
import sys
from django.urls import reverse_lazy

#from django.contrib.auth import get_user, authenticate, login

# class ProblemView(ListView):
#     model = Problems
#     template_name = 'Problems/problem.html'
def listProblems(request):
    queryset = Problems.objects.all()
    context={
        'object_list':queryset
        }
    return render(request, 'Problems/problem.html',context)

def problemDetails(request,pk):
    queryset = Problems.objects.get(id=pk)
    context={'object':queryset}
    return render(request, 'Problems/solve_section.html',context)

def addProblem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProblemForm()
    context ={
        'form':form
    }
    return render(request, 'Problems/add_problems.html', context)

def updateProblem(request,pk):
    problem = Problems.objects.get(id=pk)
    form = ProblemForm(instance=problem)
    if request.method == 'POST':
        form = ProblemForm(request.POST,instance=problem)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={
        'form':form
    }
    return render(request, 'Problems/add_problems.html', context)


def deleteProblem(request,pk):
    problem = Problems.objects.get(id=pk)
    if request.method == 'POST':
        problem.delete()
        return redirect('/')
    context ={
        'object':problem
    }
    return render(request, 'Problems/delete_problems.html', context)

@login_required
def categories(request):
    return render(request, 'Problems/categories.html')


@login_required
def delete_problems(request):
    return render(request, 'Problems/problem.html')

@login_required
def solve(request):
    return render(request, 'Problems/editor.html')
    
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
    res = render(request,'Problems/editor.html',{"code":code_part,"input":y,"output":output})
    return res


