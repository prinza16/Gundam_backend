from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from .models import Series
from .serializers import SeriesSerializer

class SetPaginationSeries(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 100

class SeriesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Series.objects.filter(is_active = 1).order_by('series_id')
    serializer_class = SeriesSerializer
    pagination_class = SetPaginationSeries

    filter_backends = [filters.SearchFilter]
    search_fields = ['series_name']

class SeriesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.filter(is_active=1)
    serializer_class = SeriesSerializer
    lookup_field = 'series_id'

    def perform_destroy(self, instance):
        if instance.is_active:
            instance.is_active = 0
            instance.save()
        else:
            pass
 

