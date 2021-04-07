from django.urls import path
from Problems import views as pviews


urlpatterns = [
    path('', pviews.categories, name='categories'),
    path('problems/', pviews.problems, name='problems'),
    path('solve/', pviews.solve, name='solve'),
    path('solve/run/', pviews.runcode),
]
