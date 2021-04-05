from django.urls import path
from User import views as uviews
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('profile/', uviews.profile, name='profile'),
    path('register/', uviews.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='User/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='User/logout.html'), name='logout'),
]