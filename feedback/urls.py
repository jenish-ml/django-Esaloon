from django.urls import path
from . import views

urlpatterns = [
    path('add_complaints/', views.add_complaints, name='add_complaints'),
    path('add_feedbacks/<int:id>/', views.add_feedbacks, name='add_feedbacks'),
    path('vw_comp/', views.vw_comp, name='vw_comp'),
    path('vw_complaints/', views.vw_complaints, name='vw_complaints'),
    path('vw_feedbacks/', views.vw_feedbacks, name='vw_feedbacks'),
]
