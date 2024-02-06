from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chatBot, name='chatBot'),
    # Add more paths here as needed
]