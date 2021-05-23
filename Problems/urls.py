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
<<<<<<< HEAD
    path('solve/run', pviews.runcode),
=======
    # path('solve-secton/run/<int:pk>', pviews.runcode),
    
>>>>>>> b8c18d301da0bf66dc8a40a11809e789f62d6b2e
    ]
