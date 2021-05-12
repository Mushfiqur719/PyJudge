from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Problems
from .forms import ProblemForm
from django.views.generic import ListView, DetailView, CreateView
import sys
from django.urls import reverse_lazy

#from django.contrib.auth import get_user, authenticate, login

class ProblemView(ListView):
    model = Problems
    template_name = 'Problems/problem.html'
    # queryset = Problems.objects.all()

class ProblemDetailView(DetailView):
    model = Problems
    template_name = 'Problems/solve_section.html'
    # queryset = Problems.objects.all()

class AddProblemView(CreateView):
    model = Problems
    template_name = 'Problems/add_problems.html'
    fields = '__all__'
    success_url = reverse_lazy('problems-list')

# class DeleteProblemView(DeleteView):
#     model = Problems
#     template_name = 'Problems/delete_problems.html'

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


