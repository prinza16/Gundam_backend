from django.shortcuts import render
from rest_framework import generics
from .models import Pilot
from .serializers import PilotSerializer

class PilotListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pilot.objects.filter(is_active = 1)
    serializer_class = PilotSerializer

class PilotRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    lookup_field = 'pilot_id'

    def perform_destroy(self, instance):
        if instance.is_active:
            instance.is_active = 0
            instance.save()
        else:
            pass


