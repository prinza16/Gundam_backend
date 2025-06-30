from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Grade
from .serializers import GradeSerializer

class SetPaginationGrade(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 100

class GradeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Grade.objects.filter(is_active=1)
    serializer_class = GradeSerializer
    pagination_class = SetPaginationGrade

class GradeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    lookup_field = 'grade_id'

    def perform_destroy(self, instance):
        if instance.is_active:
            instance.is_active = 0
            instance.save()
        else:
            pass

