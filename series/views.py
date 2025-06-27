from django.shortcuts import render
from rest_framework import generics
from .models import Series
from .serializers import SeriesSerializer

class SeriesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Series.objects.filter(is_active = 1)
    serializer_class = SeriesSerializer

class SeriesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.filter()
    serializer_class = SeriesSerializer
    lookup_field = 'series_id'

    def perform_destroy(self, instance):
        if instance.is_active:
            instance.is_active = 0
            instance.save()
        else:
            pass


