from django.contrib import admin
from django.urls import path, include
from Contestant import views as cviews
from Operator import views as oviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contestant/', include('Contestant.urls')),
    path('operator/', include('Operator.urls')),
    path('profile/',),
    path('register/',),
]
