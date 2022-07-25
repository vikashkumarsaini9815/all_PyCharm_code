from rest_framework import serializers
from P_app.models import *






class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"