from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Problems
from .forms import ProblemForm, SubmissionForm
import sys, datetime, timeit


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

@login_required
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

@login_required
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

@login_required
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
def solve(request,pk):
    problem = Problems.objects.get(id=pk)
    context ={
        'object':problem
    }
    return render(request, 'Problems/editor.html',context)
    
@login_required
def runcode(request,pk):
    problem = Problems.objects.get(id=pk)
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part = problem.sample_input
        print(input_part)
        return_input = input_part
        input_part = input_part.replace("\n"," ").split(" ")
        print(input_part)
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            start = timeit.timeit()
            exec(code_part)
            end = timeit.timeit()
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
            print(output)
        data = {
            "user": request.user.username,
            "problem_id":problem.problem_id,
            "problem_name":problem.problem_name,
            "submission_time":str(datetime.datetime.now()),
            "verdict":output,
            "run_time":str(end-start),
        }
        form = SubmissionForm(data)
        if form.is_valid():
            form.save()
        
        context={
            "code":code_part,
            "input":return_input,
            "output":output,
            "object":problem,
        }
        
    res = render(request,'Problems/editor.html',context)
    return res


