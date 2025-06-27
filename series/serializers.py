from rest_framework import serializers
from .models import Series

class SeriesSerializer(serializers.ModelSerializer):
    series_universe_name = serializers.CharField(source='series_universe.universe_name', read_only=True)
    class Meta:
        model = Series
        fields = [
            'series_id',
            'series_name',
            'series_image',
            'series_universe',
            'series_universe_name',
            'is_active',
            'create_date',
            'update_date',
        ]

        read_only_fields = ['create_date', 'update_date'] 

