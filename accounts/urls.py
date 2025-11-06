from django.urls import path
from .views import signup, profile_view, profile_update
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_update, name='profile_edit'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html', success_url='/accounts/profile/'), name='password_change'),
]