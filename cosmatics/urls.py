from django.urls import path
from . import views

urlpatterns = [
    path('add_cosmetics/', views.add_cosmetics, name='add_cosmetics'),
    path('edit_cosmetics/<int:id>/', views.edit_cosmetics, name='edit_cosmetics'),
    path('view_cosmetics/', views.view_cosmetics, name='view_cosmetics'),
    path('delete_cosmetics/<int:id>/', views.delete_cosmetics, name='delete_cosmetics'),
    path('v_saloon_cosmetics/', views.v_saloon_cosmetics, name='v_saloon_cosmetics'),
    path('v_category_cosmetics/', views.v_category_cosmetics, name='v_category_cosmetics'),
    path('v_cosmetics/<int:id>/', views.v_cosmetics, name='v_cosmetics'),
]
