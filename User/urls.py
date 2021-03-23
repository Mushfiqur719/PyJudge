from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.show_user_home_page),
    path('info/', views.show_user_info_page),
]
