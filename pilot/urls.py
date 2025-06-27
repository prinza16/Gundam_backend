from django.urls import path
from .views import PilotListCreateAPIView, PilotRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', PilotListCreateAPIView.as_view(), name='pilotlist'),
    path('<int:pilot_id>/', PilotRetrieveUpdateDestroyAPIView.as_view(), name='pilotdetail'),
]
