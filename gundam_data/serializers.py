from rest_framework import serializers
from .models import Types, Seller, ModelData, ModelPilotAssignment, ModelSeriesOccurrence, ModelImage
from grade.models import Grade
from universe.models import Universe
from series.models import Series
from pilot.models import Pilot

class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = '__all__'
        read_only_fields = ('create_date', 'update_date',)

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'
        read_only_fields = ('create_date', 'update_date',)

class ModelDataSerializer(serializers.ModelSerializer):
    model_grade_name = serializers.CharField(source='model_grade.grade_name', read_only=True)
    model_seller_name = serializers.CharField(source='model_seller.seller_name', read_only=True)
    model_type_name = serializers.CharField(source='model_type.types_name', read_only=True)
    main_image = serializers.SerializerMethodField()
    release_date = serializers.SerializerMethodField()

    class Meta:
        model = ModelData
        fields = [
            'model_id',
            'model_name',
            'model_grade',
            'model_grade_name',
            'model_seller',
            'model_seller_name',
            'model_type',
            'model_type_name',
            'model_initial',
            'release_date',
            'model_length',
            'model_width',
            'model_height',
            'main_image',
            'is_active',
            'create_date',
            'update_date',
        ]
        read_only_fields = ('create_date', 'update_date',)

    def get_main_image(self, obj):
        main_img = obj.images.filter(is_main=True).first()
        if main_img:
            return main_img.image.url
        return None

    def get_release_date(self, obj):
        if obj.model_initial:
            return obj.model_initial.strftime('%Y-%m')
        return None

class ModelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelImage
        fields = ['image', 'is_main']

class ModelPilotAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPilotAssignment
        fields = '__all__'

class ModelSeriesOccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelSeriesOccurrence
        fields = '__all__'
