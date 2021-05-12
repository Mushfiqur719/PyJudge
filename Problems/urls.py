from django.urls import path
from Problems import views as pviews
from Problems.views import ProblemView, ProblemDetailView, AddProblemView


urlpatterns = [
    path('', pviews.categories, name='categories'),
    path('solve/', pviews.solve, name='solve'),
    # path('run', pviews.runcode),
    path('add-problems/', AddProblemView.as_view(), name='add-problem'),
    path('problems-list/', ProblemView.as_view(), name='problems-list'),
    path('solve-section/<int:pk>', ProblemDetailView.as_view(), name='solve-section'),
    path('solve/run', pviews.runcode),
    
    ]
