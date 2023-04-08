from authApp.models.opinions import Opinions
from authApp.models.customers import Customers
from authApp.models.destinations import Destinations
from rest_framework import serializers
from authApp.serializers.customersSerializer import CustomersSerializer
from authApp.serializers.destinationsSerializer import DestinationsSerializer


class OpinionsSerializer(serializers.ModelSerializer):
    destination = DestinationsSerializer()
    customer = CustomersSerializer()
    destination_img = serializers.SerializerMethodField()
    customer_img = serializers.SerializerMethodField()

    class Meta:
        model = Opinions
        fields = ['opinion_id', 'comment', 'rating', 'customer', 'destination']

    def create(self, validated_data):
        destination_data = validated_data.pop('destination')
        customer_data = validated_data.pop('customer')
        destination_instance, _ = Destinations.objects.get_or_create(**destination_data)
        customer_instance, _ = Customers.objects.get_or_create(**customer_data)
        opinion_instance = Opinions.objects.create(destination_id=destination_instance, customer_id=customer_instance, **validated_data)
        return opinion_instance

    def to_representation(self, obj):
        opinion = obj
        destination = opinion.destination_id
        customer = opinion.customer_id

        if destination.destination_img:
            destination_img = destination.destination_img.url
        else:
            destination_img = None

        if customer.customer_img:
            customer_img = customer.customer_img.url
        else:
            customer_img = None

        return {
            'opinion_id': opinion.opinion_id,
            'comment': opinion.comment,
            'rating': opinion.rating,
            'destination': {
                'destination_id': destination.destination_id,
                'destination_img': destination_img,
                'country': destination.country,
                'city': destination.city,
                'cost': destination.cost,
                'discount_price': destination.discount_price,
                'average_mark': destination.average_mark
            },
            'customer': {
                'customer_id': customer.customer_id,
                'customer_img': customer_img,
                'name': customer.name,
                'last_name': customer.last_name,
                'email': customer.email
            }
        }

    def get_destination_img(self, obj):
        if obj.destination_img:
            return obj.destination_img.url
        return None

    def get_customer_img(self, obj):
        if obj.customer_img:
            return obj.customer_img.url
        return None
