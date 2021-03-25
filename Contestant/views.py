from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_contestant_home_page(request):
    return render(request, 'Contestant/home.html')

def show_contestant_info_page(request):
    return HttpResponse("My name is Contestant 1")