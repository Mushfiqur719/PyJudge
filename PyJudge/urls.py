from django.contrib import admin
from django.urls import path, include
from Contestant import views as cviews
from Judge import views as jviews
from User import views as uviews
from Home import views as hviews
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contestant/', include('Contestant.urls')),
    path('judge/', include('Judge.urls')),
    path('profile/', uviews.profile,name='profile'),
    path('register/', uviews.register,name='register'),
    path('', hviews.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='User/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='User/logout.html'),name='logout'),

]
