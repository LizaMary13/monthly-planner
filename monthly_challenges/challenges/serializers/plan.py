from rest_framework import serializers

from challenges.models import *

class PlanDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Plan
        fields = ['month', 'day', 'title', 'is_complete']
    