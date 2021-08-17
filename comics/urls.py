from django.urls import path
from . import views, series, issue

app_name = 'comics'

urlpatterns = [
    path('', views.comics_home, name='comics_home'),
    path('new-series/', series.create_series, name='create_series'),
    path('update-series/<pk>/<slug>/', series.update_series, name='update_series'),
    path('view-series/<pk>/<slug>/', series.view_series, name='view_series'),
    path('series/<s_pk>/new-issue/', issue.create_issue, name='new_issue'),
    path('series/<s_pk>/update-issue/<pk>/<slug>/', issue.update_issue, name='update_issue'),
    path('series/<s_pk>/issue/<pk>/<slug>', issue.view_issue, name='view_issue'),
]
