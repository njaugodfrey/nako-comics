from django.urls import path
from . import views, series, issue

app_name = 'comics'

urlpatterns = [
    path('', views.comics_home, name='comics_home'),
    # series
    path('new-series/', series.create_series, name='create_series'),
    path('update-series/<pk>/<slug>/', series.update_series, name='update_series'),
    path('view-series/<pk>/<slug>/', series.view_series, name='view_series'),
    # issues
    path('series/<s_pk>/new-issue/', issue.create_issue, name='new_issue'),
    path('series/<s_pk>/update-issue/<pk>/<slug>/', issue.update_issue, name='update_issue'),
    path('series/<s_pk>/issue/<pk>/<slug>/', issue.view_issue, name='view_issue'),
    # categories
    path('categories/', views.categories_list, name='all_categories'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/view/<pk>/', views.view_category, name='view_category'),
    # types
    path('types/', views.types_list, name='all_types'),
    path('types/create', views.create_type, name='create_type'),
    path('types/view/<pk>', views.view_type, name='view_type'),
]
