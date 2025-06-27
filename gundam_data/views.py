from django.shortcuts import render
from rest_framework import generics
from .models import Types, Vendor, ModelData, ModelPilotAssignment, ModelSeriesOccurrence, ModelUniverseOccurrence, 
from .serializers import TypesSerializer, VendorSerializer, ModelDataSerializer, ModelPilotAssignmentSerializer, ModelSeriesOccurrenceSerializer, ModelUniverseOccurrenceSerializer

class TypesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Types.objects.all()
    serializer_class = TypesSerializer

class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Types.objects.all()
    serializer_class = VendorSerializer

class ModelDataListCreateAPIView(generics.ListCreateAPIView):
    queryset = Types.objects.all()
    serializer_class = ModelDataSerializer



