from django.urls import path
from User import views as uviews
from . import views


urlpatterns = [
    path('', views.home, name='home'),
]
