from authApp.models.promotions import Promotions
from authApp.models.destinations import Destinations
from rest_framework import serializers
from authApp.serializers.destinationsSerializer import DestinationsSerializer


class PromotionsSerializer(serializers.ModelSerializer):
    destination = DestinationsSerializer()
    destination_img = serializers.SerializerMethodField()

    class Meta:
        model = Promotions
        fields = ['promotion_id', 'destination', 'trip_length', 'plan_cost']

    def create(self, validated_data):
        destination_data = validated_data.pop('destination')
        destination_instance = Destinations.objects.create(**destination_data)
        promotion_instance = Promotions.objects.create(destination_id=destination_instance, **validated_data)
        return promotion_instance

    def to_representation(self, obj):
        promotion = Promotions.objects.get(promotion_id=obj.promotion_id)
        destination = Destinations.objects.get(destination_id=promotion.destination_id.destination_id)
        destination_img = None
        if destination.destination_img:
            destination_img = destination.destination_img.url
        return {
            'promotion_id': promotion.promotion_id,
            'trip_length': promotion.trip_length,
            'plan_cost': promotion.plan_cost,
            'destination': {
                'destination_id': destination.destination_id,
                'destination_img': destination_img,
                'country': destination.country,
                'city': destination.city,
                'cost': destination.cost,
                'discount_price': destination.discount_price,
                'average_mark': destination.average_mark
            }
        }

    def get_destination_img(self, obj):
        if obj.destination_img:
            return obj.destination_img.url
        return None