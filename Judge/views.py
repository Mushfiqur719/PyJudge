from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def show_judge_home_page(request):
    return render(request, 'Judge/home.html')
    
@login_required
def show_judge_info_page(request):
    return HttpResponse("My name is Operator 1")