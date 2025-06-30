from django.shortcuts import render
from rest_framework import generics
from .models import Types, Vendor, ModelData, ModelPilotAssignment, ModelSeriesOccurrence, ModelUniverseOccurrence
from .serializers import TypesSerializer, VendorSerializer, ModelDataSerializer, ModelPilotAssignmentSerializer, ModelSeriesOccurrenceSerializer, ModelUniverseOccurrenceSerializer

class TypesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Types.objects.all()
    serializer_class = TypesSerializer

class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class ModelDataListCreateAPIView(generics.ListCreateAPIView):
    queryset = ModelData.objects.all()
    serializer_class = ModelDataSerializer

class ModelPilotAssignmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = ModelPilotAssignment.objects.all()
    serializer_class = ModelPilotAssignmentSerializer

class ModelSeriesOccurrenceListCreateAPIView(generics.ListCreateAPIView):
    queryset = ModelSeriesOccurrence.objects.all()
    serializer_class = ModelSeriesOccurrenceSerializer

class ModelUniverseOccurrenceListCreateAPIView(generics.ListCreateAPIView):
    queryset = ModelUniverseOccurrence.objects.all()
    serializer_class = ModelUniverseOccurrenceSerializer


