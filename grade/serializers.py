from rest_framework import serializers
from .models import Grade

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = [
            'grade_id',
            'grade_name',
            'is_active',
            'create_date',
            'update_date'
        ]

        read_only_fields = ['create_date', 'update_date']