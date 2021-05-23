from django.urls import path
from Contest import views as cviews
<<<<<<< HEAD
from .views import TutorialView, TutorialDetailView, AddContestView, ContestView, ContestDetailView, AddTutorialView
=======
from .views import TutorialView, TutorialDetailView, AddContestView, ContestView, ContestDetailView
>>>>>>> b8c18d301da0bf66dc8a40a11809e789f62d6b2e


urlpatterns = [
    # path('', cviews.contest, name='contest'),
    path('', ContestView.as_view(), name='contest-list'),
    path('tutorials-list/', TutorialView.as_view(), name='tutorials-list'),
    path('tutorials/<int:pk>', TutorialDetailView.as_view(),name='tutorials'),
<<<<<<< HEAD
    path('add-tutorials/', AddTutorialView.as_view(), name='add-tutorials'),
=======
>>>>>>> b8c18d301da0bf66dc8a40a11809e789f62d6b2e
    path('add-contest/', AddContestView.as_view(), name='add-contest'),
    path('contest-section/<int:pk>', ContestDetailView.as_view(), name='contest-section'),
    
]
