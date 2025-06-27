from rest_framework import serializers
from .models import Types, Vendor, ModelData, ModelPilotAssignment, ModelSeriesOccurrence, ModelUniverseOccurrence
from grade.models import Grade
from universe.models import Universe
from series.models import Series
from pilot.models import Pilot

class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = '__all__'
        read_only_fields = ('create_date', 'update_date',)

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = ('create_date', 'update_date',)

class ModelDataSerializer(serializers.ModelSerializer):
    model_grade_name = serializers.CharField(source='model_grade.grade_name', read_only=True)
    class Meta:
        model = ModelData
        fields = [
            'model_id',
            'model_name',
            'model_image',
            'model_grade',
            'model_grade_name',
            'model_initial',
            'model_length',
            'model_width',
            'model_height',
            'is_active',
            'create_date',
            'update_date',
        ]
        read_only_fields = ('create_date', 'update_date',)

class ModelPilotAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPilotAssignment
        fields = '__all__'

class ModelSeriesOccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelSeriesOccurrence
        fields = '__all__'

class ModelUniverseOccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelUniverseOccurrence
        fields = '__all__'