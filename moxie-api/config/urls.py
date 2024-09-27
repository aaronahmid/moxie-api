"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authentication import BasicAuthentication
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Booking System Service",
        default_version="v1.2",
        description="for booking, order and invoice management",
        terms_of_service="",
        contact=openapi.Contact(email="techteam@aajexpress.org"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=[permissions.IsAuthenticated],
    authentication_classes=[BasicAuthentication],
)

# api url mappings
api = [
    path("", include("services.appointments.urls", namespace="appointments")),
    path("", include("services.medspas.urls", namespace="medspa")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = [
    # version api endpoints
    path("api/", include(api), name="api"),
    # path("swagger.json/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    # path(
    #     "",
    #     schema_view.with_ui("swagger", cache_timeout=0),
    #     name="schema-swagger-ui",
    # ),
    # path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
]