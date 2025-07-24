from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Types, Seller, ModelData, ModelPilotAssignment, ModelSeriesOccurrence, ModelImage
from .serializers import TypesSerializer, SellerSerializer, ModelDataSerializer, ModelPilotAssignmentSerializer, ModelSeriesOccurrenceSerializer, ModelImageSerializer

class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 100

class TypesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Types.objects.filter(is_active = 1).order_by('types_id')
    serializer_class = TypesSerializer
    pagination_class = StandardPagination

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
    pagination_class = StandardPagination

    filter_backends = [filters.SearchFilter]
    search_fields = ['seller_name']

class SellerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.filter(is_active=1)
    serializer_class = SellerSerializer
    lookup_field = 'seller_id'

    def perform_destroy(self, instance):
        if instance.is_active:
            instance.is_active = 0
            instance.save()
        else:
            pass

class ModelDataListCreateAPIView(generics.ListCreateAPIView):
    queryset = ModelData.objects.filter(is_active = 1).order_by('model_id')
    serializer_class = ModelDataSerializer
    pagination_class = StandardPagination

    filter_backends = [filters.SearchFilter]
    search_fields = ['model_name']

class ModelDataRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ModelData.objects.filter(is_active = 1)
    serializer_class = ModelDataSerializer
    lookup_field = 'model_id'

    def perform_destroy(self, instance):
        if instance.is_active:
            instance.is_active = 0
            instance.save()
        else: 
            pass

class ModelImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = ModelImage.objects.all()
    serializer_class = ModelImageSerializer
    parser_classes = (MultiPartParser, FormParser)

class ModelPilotAssignmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = ModelPilotAssignment.objects.all()
    serializer_class = ModelPilotAssignmentSerializer

class ModelSeriesOccurrenceListCreateAPIView(generics.ListCreateAPIView):
    queryset = ModelSeriesOccurrence.objects.all()
    serializer_class = ModelSeriesOccurrenceSerializer



