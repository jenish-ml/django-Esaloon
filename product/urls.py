from django.urls import path
from . import views

urlpatterns = [
    path('addproduct/', views.add_product, name='add_product'),
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),
    path('view_product/', views.view_product, name='view_product'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('freelance_addproduct/', views.freelance_add_product, name='freelance_add_product'),
    path('freelance_view_product/', views.freelance_view_product, name='freelance_view_product'),
    path('edit_freelance_product/<int:id>/', views.edit_freelance_product, name='edit_freelance_product'),
    path('delete_freelance_product/<int:id>/', views.delete_freelance_product, name='delete_freelance_product'),
    path('v_saloon_product/<int:id>/', views.v_saloon_product, name='v_saloon_product'),
    path('v_fw_product/<int:id>/', views.v_fw_product, name='v_fw_product'),
]
