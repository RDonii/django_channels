from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<channel_key>', views.room)
]