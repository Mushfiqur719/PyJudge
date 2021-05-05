from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home,name='contestant-home'),
    path('about-us/', views.about_us, name='about-us'),
]
