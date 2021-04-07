from django.urls import path
from User import views as uviews
from Home import views as hviews


urlpatterns = [
    path('', hviews.home, name='home'),
    path('solve/', hviews.solve, name='solve'),
    path('run', hviews.runcode),

]
