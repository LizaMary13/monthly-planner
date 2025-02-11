from rest_framework import serializers

from challenges.models import *

class MonthDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Month
        fields = ['month', 'year']
    