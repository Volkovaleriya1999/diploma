from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.tours, name='tours'),
    path('tour_details/<int:pk>/', views.tour, name='tour'),
]