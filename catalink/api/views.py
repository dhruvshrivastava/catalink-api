from django.shortcuts import render
from api.serializers import ProductUserSerializer, ProductSerializer, CategorySerializer
from api.models import Product, Category, ProductUser
from rest_framework import generics
from rest_framework.response import Response

class ProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        products = Product.objects.all()
        return Response('Nonetype for now')
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            product_name = serializer.data.get('product_name')
            product_price = serializer.data.get('product_price')
            product_description = serializer.data.get('product_description')
            # check if category queryset exists 
            category_name = serializer.data.get('product_category').get('category_name')
            queryset = Category.objects.filter(category_name=category_name)
            category = None
            if queryset:
                category = Category.objects.filter(category_name=category_name)[0]
                product = Product.objects.create(product_name=product_name, product_description=product_description, product_price=product_price, product_category=category)
                return Response('Product OK')
            else:
                return Response('FAILED')

class CategoryView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get(self, request, format=None):
        categorys = Category.objects.all()
        return Response("None type for now")
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            category_name = serializer.data.get('category_name')
            # check if user queryset exists 
            username = serializer.data.get('owner').get('username')
            email = serializer.data.get('owner').get('email')
            queryset = ProductUser.objects.filter(username=username, email=email)[0]
            owner = None
            if queryset:
                owner = ProductUser.objects.filter(username=username, email=email)[0]
                category = Category.objects.create(category_name = category_name, owner = owner)
                return Response('Category OK')
            else:
                return Response('FAILED')

class ProductUserView(generics.CreateAPIView):
    queryset = ProductUser.objects.all()
    serializer_class = ProductUserSerializer

    def get(self, request, format=None):
        users = ProductUser.objects.all()
        return Response('OK')
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            email = serializer.data.get('email')
            user = ProductUser.objects.create(username=username, email=email)
            
            return Response('User OK')