from authApp.models.customers import Customers
from rest_framework import serializers


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['customer_id', 'customer_img', 'name', 'last_name', 'email']
