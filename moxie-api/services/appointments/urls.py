#!/usr/bin/env python3
"""medspa api url mappings"""
from .api.endpoints import AppointmentViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

app_name = "appointments"

router = DefaultRouter()
router.register("appointments", AppointmentViewSet, basename="appointments")

urlpatterns = []
urlpatterns += router.urls
