from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.show_contestant_home_page),
    path('info/', views.show_contestant_info_page),
]
