from django.urls import path
from .views import UniverseListCreateAPIView, UniverseRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', UniverseListCreateAPIView.as_view(), name='universelist'),
    path('<int:universe_id>/', UniverseRetrieveUpdateDestroyAPIView.as_view(), name='universedetail')
]
