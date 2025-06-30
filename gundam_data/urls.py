from django.urls import path
from .views import TypesListCreateAPIView, VendorListCreateAPIView, ModelDataListCreateAPIView, ModelPilotAssignmentListCreateAPIView, ModelSeriesOccurrenceListCreateAPIView, ModelUniverseOccurrenceListCreateAPIView 

urlpatterns = [
    path('', ModelDataListCreateAPIView.as_view(), name='gundamlist'),
    path('types/', TypesListCreateAPIView.as_view(), name='typeslist'),
    path('vendors/', VendorListCreateAPIView.as_view(), name='vendorlist'),
    path('model-pilot-assignments/', ModelPilotAssignmentListCreateAPIView.as_view(), name='modelpilotlist'),
    path('model-series-occurrences/', ModelSeriesOccurrenceListCreateAPIView.as_view(), name='modelserieslist'),
    path('model-universe-occurrences/', ModelUniverseOccurrenceListCreateAPIView.as_view(), name='modeluniverselist')
]


