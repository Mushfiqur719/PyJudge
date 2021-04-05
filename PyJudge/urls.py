from django.contrib import admin
from django.urls import path, include
from Contestant import views as cviews
from Judge import views as jviews
from Home import views as hviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hviews.home,name='home'),
    path('user/', include('User.urls')),
    path('contestant/', include('Contestant.urls')),
    path('judge/', include('Judge.urls')),
]
