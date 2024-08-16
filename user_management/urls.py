from django.urls import path
from . import views

urlpatterns = [
    path('view_freelance_worker/', views.view_freelance_worker, name='view_freelance_worker'),
    path('view_salooner/', views.view_salooner, name='view_salooner'),
    path('near_by_saloon/', views.near_by_saloon, name='near_by_saloon'),
    path('near_by_fre/', views.near_by_fre, name='near_by_fre'),
    path('profile/', views.profile, name='profile'),
    path('edit_prof/<int:id>/', views.edit_prof, name='edit_prof'),
    path('edit_prof_fre/<int:id>/', views.edit_prof_fre, name='edit_prof_fre'),
    path('edit_profile/<int:id>/', views.edit_profile, name='edit_profile'),
    path('add_location/', views.add_location, name='add_location'),
]
