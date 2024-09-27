
"""order service api url mappings"""
from django.urls import path, include

app_name = "appointments"

urlpatterns = [
    path("", include("services.appointments.urls", "appointments")),
]
