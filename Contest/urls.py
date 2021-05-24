from django.urls import path
from Contest import views as cviews
from .views import TutorialView, TutorialDetailView, AddContestView, ContestView, ContestDetailView, AddTutorialView


urlpatterns = [
    # path('', cviews.contest, name='contest'),
    path('', ContestView.as_view(), name='contest-list'),
    path('tutorials-list/', TutorialView.as_view(), name='tutorials-list'),
    path('tutorials/<int:pk>', TutorialDetailView.as_view(),name='tutorials'),
    path('add-tutorials/', AddTutorialView.as_view(), name='add-tutorials'),
    path('add-contest/', AddContestView.as_view(), name='add-contest'),
    path('contest-section/<int:pk>', ContestDetailView.as_view(), name='contest-section'),
    
]
