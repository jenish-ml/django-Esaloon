from django.urls import path
from . import views

urlpatterns = [
    path('add_job/', views.add_job, name='add_job'),
    path('vw_job/', views.vw_job, name='vw_job'),
    path('delete_job/<int:id>/', views.delete_job, name='delete_job'),
    path('vw_job_fw/', views.vw_job_fw, name='vw_job_fw'),
]
