from django.contrib.auth.models import User 
from rest_framework import serializers 
from api.models import Product, Category, User
from django.contrib.auth.hashers import make_password


class ProductUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    slug = serializers.SlugField()
    password = serializers.CharField()

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return User.objects.create(**validated_data)

class CategorySerializer(serializers.Serializer):

    owner = ProductUserSerializer()    
    category_name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

class ProductSerializer(serializers.Serializer):
    owner = ProductUserSerializer()
    product_category = CategorySerializer()
    product_name = serializers.CharField(max_length=100)
    product_description = serializers.CharField(max_length=1000)
    product_price = serializers.IntegerField()
    image = serializers.ImageField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

