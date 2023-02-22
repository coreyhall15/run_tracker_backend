from .models import Run
from rest_framework import serializers

class RunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Which model will get serialized by this class
        model = Run
        # Which fields should be included in the output
        fields = ['id', 'subject', 'details']