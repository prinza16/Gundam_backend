from django.urls import path
from .views import TypesListCreateAPIView, TypeRetrieveUpdateDestroyAPIView, SellerListCreateAPIView, SellerRetrieveUpdateDestroyAPIView, ModelDataListCreateAPIView, ModelDataRetrieveUpdateDestroyAPIView, ModelPilotAssignmentListCreateAPIView, ModelSeriesOccurrenceListCreateAPIView

urlpatterns = [
    path('', ModelDataListCreateAPIView.as_view(), name='gundamlist'),
    path('<int:model_id>/', ModelDataRetrieveUpdateDestroyAPIView.as_view(), name='gundamdetail'),
    path('types/', TypesListCreateAPIView.as_view(), name='typeslist'),
    path('types/<int:types_id>/', TypeRetrieveUpdateDestroyAPIView.as_view(), name='typesdetail'),
    path('seller/', SellerListCreateAPIView.as_view(), name='sellerlist'),
    path('seller/<int:seller_id>/', SellerRetrieveUpdateDestroyAPIView.as_view(), name='sellerdetail'),
    path('model-pilot-assignments/', ModelPilotAssignmentListCreateAPIView.as_view(), name='modelpilotlist'),
    path('model-series-occurrences/', ModelSeriesOccurrenceListCreateAPIView.as_view(), name='modelserieslist'),
]


