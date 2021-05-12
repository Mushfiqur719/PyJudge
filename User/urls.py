from django.urls import path
from User import views as uviews
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', uviews.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='User/login.html'), name='login'),
    path('profile/', uviews.profile, name='profile'),
    path('profile/update/', uviews.profile_update, name='profile-update'),
    path('register/', uviews.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='User/logout.html'), name='logout'),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='User/change_pass.html'), name='change-password'),
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='User/pass_done.html'), name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='User/reset_password.html'), name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]