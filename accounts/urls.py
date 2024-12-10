from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('set-availability/', views.set_availability, name='set_availability'),
    path('home/', views.home, name='home'),
]
