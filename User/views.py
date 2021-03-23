from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_user_home_page(request):
    return render(request, 'User/home.html')

def show_user_info_page(request):
    return HttpResponse("My name is User 1")