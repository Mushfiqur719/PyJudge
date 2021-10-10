from django.urls import path
from Problems import views as pviews


urlpatterns = [
    path('categories/', pviews.categories, name='categories'),
    path('add/', pviews.addProblem, name='add-problem'),
    path('update/<str:pk>', pviews.updateProblem, name='update-problem'),
    path('delete/<str:pk>', pviews.deleteProblem, name='delete-problem'),
    path('problems-list/', pviews.listProblems, name='problems-list'),
    path('solve-section/<str:pk>', pviews.problemDetails, name='solve-section'),
    path('solve/<str:pk>', pviews.solve, name='solve'),
    path('run/<str:pk>', pviews.runcode,name='run'),
    ]
