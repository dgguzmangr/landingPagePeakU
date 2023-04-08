from authApp.models.destinations import Destinations
from rest_framework import serializers


class DestinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinations
        fields = ['destination_id', 'destination_img', 'country', 'city', 'cost', 'discount_price', 'average_mark']
