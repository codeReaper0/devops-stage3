from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_mail),  # Single endpoint for both actions
]
