from rest_framework import serializers
from ..models import Project

class ProjectSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description'
        ]
