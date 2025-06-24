from django.shortcuts import render
from rest_framework import generics
from .models import Grade
from .serializers import GradeSerializer

class GradeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class GradeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    lookup_field = 'grade_id'

