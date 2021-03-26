from django.contrib import admin
from django.urls import path, include
from Contestant import views as cviews
from Judge import views as jviews
from User import views as uviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contestant/', include('Contestant.urls')),
    path('judge/', include('Judge.urls')),
    path('profile/', uviews.profile),
    path('register/', uviews.register),
]
