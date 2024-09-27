from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
import uuid


class MedSpa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="medspas")
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email_address = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    CATEGORY_CHOICES = [
        ("FACIAL", "Facial"),
        ("INJECTABLES", "Injectables"),
        ("PEELS", "Peels")
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medspa = models.OneToOneField(
        "Medspa", on_delete=models.CASCADE, related_name="services"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    duration = models.DurationField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True)
    service_type = models.CharField(max_length=75, blank=True)

    def __str__(self):
        return self.name


class CustomerProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="customer_profile"
    )
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medspa = models.ForeignKey(
        MedSpa, on_delete=models.CASCADE, related_name="appointments"
    )
    services = models.ManyToManyField(
        Service, related_name="appointments", blank=True
    )  # Many-to-many relationship with Service
    start_time = models.DateTimeField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="scheduled"
    )

    @property
    def total_duration(self):
        return (
            self.services.aggregate(total_duration=Sum("duration"))["total_duration"]
            or 0
        )

    @property
    def total_price(self):
        return self.services.aggregate(total_price=Sum("price"))["total_price"] or 0

    def __str__(self):
        return f"Appointment at {self.medspa.name} on {self.start_time} with status {self.status}"
