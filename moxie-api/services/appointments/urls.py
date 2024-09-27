
#!/usr/bin/env python3
"""order service api url mappings"""
from django.urls import path, include

app_name = "receipts"

urlpatterns = [
    path("", include("services.receipts.api.urls", "v1")),
]
