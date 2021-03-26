from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.show_judge_home_page),
    path('info/', views.show_judge_info_page),
]
