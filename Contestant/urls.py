from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home,name='contestant-home'),
    path('info/', views.show_contestant_info_page),
]
