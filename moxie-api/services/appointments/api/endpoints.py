from rest_framework import viewsets, permissions
from rest_framework.response import Response
from core.models import MedSpa, Service, Appointment

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def retreive(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)