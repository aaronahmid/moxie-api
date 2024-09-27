from rest_framework import viewsets, permissions
from rest_framework.response import Response
from core.models import MedSpa, Service, Appointment
from services.appointments.api.serializers import AppointmentSerializer
from .serializers import MedSpaSerializer, ServiceSerializer
from rest_framework.decorators import action
from rest_framework import status

# MedSpa ViewSet
class MedSpaViewSet(viewsets.ViewSet, viewsets.ModelViewSet):
    queryset = MedSpa.objects.all()
    serializer_class = MedSpaSerializer
    permission_classes = [permissions.IsAuthenticated]
    # access_policy
    lookup_field = "id"
    http_method_names = ["get", "post", "head", "delete", "put"]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def retreive(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=["get"])
    def appointments(self, request, *args, **kwargs):
        medspa = self.get_object()
        appointments = Appointment.objects.filter(medspa=medspa)
        data = AppointmentSerializer(appointments, many=True)
        response = Response(data=data, status=status.HTTP_200_OK)
        return response


# Service ViewSet
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def retreive(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


    
