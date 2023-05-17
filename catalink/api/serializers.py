from django.contrib.auth.models import User 
from rest_framework import serializers 
from api.models import Product, Category, ProductUser


class ProductUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    def create(self, validated_data):
        return ProductUser.objects.create(**validated_data)

class CategorySerializer(serializers.Serializer):

    owner = ProductUserSerializer()    
    category_name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

class ProductSerializer(serializers.Serializer):
    product_category = CategorySerializer()
    product_name = serializers.CharField(max_length=100)
    product_description = serializers.CharField(max_length=1000)
    product_price = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

