from rest_framework import serializers
from .models import Pilot

class PilotSerializer(serializers.ModelSerializer):
    pilot_universe_name = serializers.CharField(source='pilot_universe.universe_name', read_only=True)
    class Meta:
        model = Pilot
        fields = [
            'pilot_id',
            'pilot_name',
            'pilot_image',
            'pilot_vehicle',
            'pilot_universe',
            'pilot_universe_name',
            'is_active',
            'create_date',
            'update_date',
        ]

        read_only_fields = ['create_date', 'update_date']