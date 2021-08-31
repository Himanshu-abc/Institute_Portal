from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('members_home/', views.members_home, name='members_home'),
    path('register/', views.registration, name='register'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutuser, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='members/reset_password.html'),name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='members/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='members/password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='members/password_reset_done.html'),name='password_reset_complete'),
    path('profile/', views.profile_home, name='profile'),
    path('updateprofile/', views.view_and_update_profile, name='updateprofile'),
    path('profile_view/',views.profile_view, name='profile_view'),

]