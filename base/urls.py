from django.urls import path
from . import views

#Handles all routing in the webpage
urlpatterns = [
    path('', views.lobby),
    path('room/', views.room),
]