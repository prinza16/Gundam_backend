from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from .models import Universe
from .serializers import UniverseSerializer

class SetPaginationUniverse(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 100

class UniverseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Universe.objects.filter(is_active=1).order_by('universe_id')
    serializer_class = UniverseSerializer
    pagination_class = SetPaginationUniverse

    filter_backends = [filters.SearchFilter]
    search_fields = ['universe_name']

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

