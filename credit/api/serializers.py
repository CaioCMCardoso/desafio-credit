from rest_framework import serializers
from api.models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'exp_date',
            'holder',
            'number',
            'cvv',
            'brand',
            'created_at'
        ]