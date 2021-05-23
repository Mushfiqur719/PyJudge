from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from .models import Tutorials,Contest
from django.urls import reverse_lazy
#from django.contrib.auth import get_user, authenticate, login

# @login_required
# def contest(request):
#     return render(request, 'Contest/contest_list.html')

class TutorialView(ListView):
    model = Tutorials
    template_name = 'Contest/tutorials_list.html'

class TutorialDetailView(DetailView):
    model = Tutorials
    template_name = 'Contest/tutorials.html'

<<<<<<< HEAD
class AddTutorialView(CreateView):
    model = Tutorials
    template_name = 'Contest/add_tutorials.html'
    fields = '__all__'
    success_url = reverse_lazy('tutorials-list')

=======
>>>>>>> b8c18d301da0bf66dc8a40a11809e789f62d6b2e
class ContestView(ListView):
    model = Contest
    template_name = 'Contest/contest_list.html'

class ContestDetailView(DetailView):
    model = Contest
    template_name = 'Contest/contest_section.html'
class AddContestView(CreateView):
    model = Contest
    template_name = 'Contest/add_contests.html'
    fields = '__all__'
    success_url = reverse_lazy('contest-list')




