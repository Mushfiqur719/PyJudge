from django.urls import path
from Problems import views as pviews


urlpatterns = [
    path('', pviews.categories, name='categories'),
    path('problems/', pviews.problems, name='problems'),
    path('add-problems/', pviews.add_problems,name='add-problem'),
    ]
