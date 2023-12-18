from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    def validate(self, value):
        if len(value) > 50:
            raise serializers.ValidationError('title length more than 50')
        return value
    # def validate(self, attrs):
    #     return super().validate(attrs)