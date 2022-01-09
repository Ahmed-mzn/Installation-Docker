from rest_framework import serializers
from datetime import datetime
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    #created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Product
        fields = ["id", "name", "description", "qty", "created_at"]