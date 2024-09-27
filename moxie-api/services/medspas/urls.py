#!/usr/bin/env python3
"""medspa api url mappings"""
from .api.endpoints import MedSpaViewSet, ServiceViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

app_name = "medaspas"

router = DefaultRouter()
router.register("medspas", MedSpaViewSet, basename="medspas")
router.register("services", ServiceViewSet, basename="services")

urlpatterns = []
urlpatterns += router.urls
