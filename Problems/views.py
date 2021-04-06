from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import get_user, authenticate, login


def problems(request):
    return render(request, 'Problems/problems.html')

def categories(request):
    return render(request, 'Problems/categories.html')
