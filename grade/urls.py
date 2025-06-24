from django.urls import path
from .views import Grade
from .views import GradeListCreateAPIView, GradeRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', GradeListCreateAPIView.as_view(), name='gradelist'),
    path('<int:grade_id>/', GradeRetrieveUpdateDestroyAPIView.as_view(), name='gradedetail')
]


