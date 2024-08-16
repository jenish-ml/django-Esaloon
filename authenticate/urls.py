from django.urls import path
from . import views

urlpatterns = [
    path('approval/', views.approval, name='approval'),
    path('appro/<int:id>/', views.appro, name='appro'),
    path('reject/<int:id>/', views.reject, name='reject'),
    path('manage_saloon/', views.managesaloon, name='manage_saloon'),
    path('managef/', views.managef, name='managef'),
    path('manage_seller/', views.manage_seller, name='manage_seller'),
    path('delete/<int:id>/', views.deletesaloon, name='delete_saloon'),
    path('deletef/<int:id>/', views.deletef, name='deletef'),
]
