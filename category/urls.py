from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.categorys, name='categorys'),
    path('view_category/', views.view_category, name='view_category'),
    path('edit_cat/<int:id>/', views.edit_cat, name='edit_cat'),
    path('delete_cat/<int:id>/', views.delete_cat, name='delete_cat'),
]
