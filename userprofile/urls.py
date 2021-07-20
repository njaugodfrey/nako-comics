from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    create_profile, view_profile, update_profile,
    update_account
)

app_name = 'userprofile'

urlpatterns = [
    path(
        'login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'),
        name='login'
    ),
    path(
        'logout',auth_views.LogoutView.as_view(next_page='/'),
        name='logout'
    ),
    path('signup/', create_profile, name='create-profile'),
    path('view/<slug>-<pk>/', view_profile, name='view-profile'),
    path('update-profile/<slug>-<pk>/', update_profile, name='update-profile'),
    path('update-account/<slug>-<pk>/', update_account, name='update-account'),
]
