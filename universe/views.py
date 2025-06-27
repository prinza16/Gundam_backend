from django.shortcuts import render
from rest_framework import generics
from .models import Universe
from .serializers import UniverseSerializer

class UniverseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Universe.objects.filter(is_active=1)
    serializer_class = UniverseSerializer

class UniverseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Universe.objects.filter(is_active=1)
    serializer_class = UniverseSerializer
    lookup_field = 'universe_id'

    def perform_destroy(self, instance):
        if instance.is_active:
            instance.is_active = 0
            instance.save()
        else:
            pass

