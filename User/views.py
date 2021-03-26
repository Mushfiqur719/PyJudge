from django.shortcuts import render


def profile(request):
    context = {
        'name': "Mushfiqur",
        'email': "rahmanmushfiqur719@gmail.com",
        'problem_solved': ['309', '310', '405', '210']
    }
    return render(request, 'user/profile.html', context)


def register(request):
    return render(request, 'user/register.html')