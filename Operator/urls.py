from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.show_operator_home_page),
    path('info/', views.show_operator_info_page),
]
