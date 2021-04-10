from django.urls import path
from Problems import views as pviews
from Problems.views import ProblemView, ProblemDetailView


urlpatterns = [
    path('', pviews.home, name='home'),
    path('solve/', pviews.solve, name='solve'),
    path('run', pviews.runcode),
    path('categories/', pviews.categories, name='categories'),
    path('problems/', ProblemView.as_view(), name='problems'),
    path('add-problems/', pviews.add_problems, name='add-problem'),
    # path('solve/<int:pk>', ProblemDetailView.as_view(), name='solve'),

    ]
