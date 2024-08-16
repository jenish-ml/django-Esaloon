from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('reg/', views.reg, name='register'),
    path('cos_reg/', views.cos_reg, name='cos_register'),
    path('login/', views.Login, name='login'),
    path('workerreg/', views.workerreg, name='worker_register'),
    path('saloonreg/', views.saloonreg, name='saloon_register'),
    path('logout/', views.Logout, name='logout'),  # Make sure this matches the view name
    path('forgot_password/', views.forgot_password, name='forgot_password'),
]
