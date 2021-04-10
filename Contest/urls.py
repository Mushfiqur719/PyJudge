from django.urls import path
from Contest import views as cviews
from .views import TutorialView


urlpatterns = [
    path('', cviews.contest, name='contest'),
    path('tutorials/', TutorialView.as_view(), name='tutorials'),
]
