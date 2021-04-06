from django.urls import path
from Contest import views as cviews


urlpatterns = [
    path('', cviews.contest, name='contest'),
    path('tutorials/', cviews.tutorials, name='tutorials'),
]
