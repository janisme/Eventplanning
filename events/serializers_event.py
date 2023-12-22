from rest_framework import serializers
from .models import Event  # Adjust this import based on your actual model location

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    # Add any additional validation or customization here if needed
