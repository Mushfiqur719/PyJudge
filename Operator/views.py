from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_operator_home_page(request):
    return render(request, 'Operator/home.html')

def show_operator_info_page(request):
    return HttpResponse("My name is User 1")