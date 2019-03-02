from rest_framework import serializers
from .models import validated

class validatedserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = validated
        fields = (
            'name',
            'source',
            'destination',
            'type',
            'url'
        )
