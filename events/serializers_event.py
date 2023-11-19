from rest_framework import serializers
from .models import Event

class eventserializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields =[
            'event_id',
            'event_title',
            'holder_id',
            'e_date',
            #'capacity',
            #'e_complete',
            'e_detail',
        ]