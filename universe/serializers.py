from rest_framework import serializers
from .models import Universe

class UniverseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universe
        fields = [
            'universe_id',
            'universe_name',
            'is_active',
            'create_date',
            'update_date'
        ]

        read_only_fields = ['create_date', 'update_date'] 