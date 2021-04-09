from django.contrib import admin
from django.urls import path, include
from User import views as uviews
from Contestant import views as cviews
from Judge import views as jviews
from Home import views as hviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('Home.urls')),
    path('',include('User.urls')),
    path('contestant/', include('Contestant.urls')),
    path('judge/', include('Judge.urls')),
    path('contest/',include('Contest.urls')),
    path('problems/',include('Problems.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
