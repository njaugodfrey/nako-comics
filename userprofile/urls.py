from django.urls import path

from .views import create_profile, view_profile, update_profile

urlpatterns = [
    path('', create_profile, name='create-profile'),
    path('view/<slug>-<pk>/', view_profile, name='view-profile'),
    path('update/<slug>-<pk>/', update_profile, name='update-profile'),
]
