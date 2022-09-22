from rest_framework import serializers
from .models import *



class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = [
            'roi',
        ]
