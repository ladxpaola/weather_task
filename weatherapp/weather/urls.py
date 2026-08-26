from django.urls import path
from . import views

urlpatterns = [
    path("", views.weather_json, name="weather"),
]