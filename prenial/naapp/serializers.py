from rest_framework import serializers
from .models import cricket

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model=cricket
        fields='__all__'