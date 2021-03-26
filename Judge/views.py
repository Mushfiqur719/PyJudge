from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_judge_home_page(request):
    return render(request, 'Judge/home.html')

def show_judge_info_page(request):
    return HttpResponse("My name is Operator 1")