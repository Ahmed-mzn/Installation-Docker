from rest_framework import serializers
from datetime import datetime
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "qty", "get_created_at"]
