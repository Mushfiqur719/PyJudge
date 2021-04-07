from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import sys
#from django.contrib.auth import get_user, authenticate, login

@login_required
def home(request):
    return render(request, 'user/home.html',)

def solve(request):
    return render(request, 'Home/solve.html')

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
    res = render(request,'Home/solve.html',{"code":code_part,"input":y,"output":output})
    return res

