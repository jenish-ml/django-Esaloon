from django.urls import path
from . import views

urlpatterns = [
    path('v_today_book/', views.v_today_book, name='v_today_book'),
    path('payment/<int:id>/', views.payment, name='payment'),
    path('my_bookings/', views.my_booking, name='my_booking'),
    path('todaysBooking/', views.todaysBooking, name='todaysBooking'),
    path('book_all/', views.book_all, name='book_all'),
    path('cart/<int:id>/', views.cart, name='cart'),
    path('my_cart/', views.my_cart, name='my_cart'),
    path('feedbacks/', views.feedbacks, name='feedbacks'),
    path('add_feedback/', views.add_feedback, name='add_feedback'),
]
