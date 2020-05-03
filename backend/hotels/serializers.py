from .models import Package
from rest_framework import serializers

class PackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'hotel', 'price', 'duration', 'valid_until', 'description']