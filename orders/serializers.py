from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
            model = Order
            fields = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'postal_code', 'city', 'created', 'updated', 'paid', 'coupon')


