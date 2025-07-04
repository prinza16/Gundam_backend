from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from .models import Types, Seller, ModelData, ModelPilotAssignment, ModelSeriesOccurrence, ModelUniverseOccurrence
from .serializers import TypesSerializer, SellerSerializer, ModelDataSerializer, ModelPilotAssignmentSerializer, ModelSeriesOccurrenceSerializer, ModelUniverseOccurrenceSerializer

class SetPaginationSeries(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 100

class TypesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Types.objects.filter(is_active = 1).order_by('types_id')
    serializer_class = TypesSerializer
    pagination_class = SetPaginationSeries

    filter_backends = [filters.SearchFilter]
    search_fields = ['types_name']

class TypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Types.objects.filter(is_active=1)
    serializer_class = TypesSerializer
    lookup_field = 'types_id'

    def perform_destroy(self, instance):
        if instance.is_active:
            instance.is_active = 0
            instance.save()
        else:
            pass

class SellerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Seller.objects.filter(is_active = 1).order_by('seller_id')
    serializer_class = SellerSerializer
    pagination_class = SetPaginationSeries

    filter_backends = [filters.SearchFilter]
    search_fields = ['seller_name']

class SellerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.filter(is_active=1)
    serializer_class = TypesSerializer
    lookup_field = 'seller_id'

    def perform_destroy(self, instance):
        if instance.is_active:
            instance.is_active = 0
            instance.save()
        else:
            pass

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


