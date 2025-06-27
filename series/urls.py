from django.urls import path
from .views import SeriesListCreateAPIView, SeriesRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', SeriesListCreateAPIView.as_view(), name='serieslist'),
    path('<int:series_id>/', SeriesRetrieveUpdateDestroyAPIView.as_view(), name='seriesdetail')
]
