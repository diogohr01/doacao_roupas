# serializers.py

from rest_framework import serializers
from feedback.models import Feedback
from django.db.models import Avg

class FeedbackSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Feedback
        fields = ['id', 'doador',  'descricao', 'rate', 'stars']
        
        def create(self, validated_data):
            doador = validated_data.get('doador')
            
            

    def get_rate(self, obj):
        rate = Feedback.objects.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None