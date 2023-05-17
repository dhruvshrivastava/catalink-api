from django.shortcuts import render
from api.serializers import ProductUserSerializer, ProductSerializer, CategorySerializer
from api.models import Product, Category
from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import json 
from django.contrib.auth import get_user_model 
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

User = get_user_model()

class ProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request, format=None):
        """
        Return a list of all products
        """
        products = Product.objects.all().values()
        return JsonResponse({"products":list(products)})
        #return Response("OK")
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            product_name = serializer.data.get('product_name')
            product_price = serializer.data.get('product_price')
            product_description = serializer.data.get('product_description')
            image = request.data['file']
            # check if category queryset exists 
            category_name = serializer.data.get('product_category').get('category_name')
            queryset = Category.objects.filter(category_name=category_name)
            category = None
            # check if user queryset exists 
            username = serializer.data.get('owner').get('username')
            email = serializer.data.get('owner').get('email')
            slug = serializer.data.get('owner').get('slug')
            password = serializer.data.get('owner').get('password')
            print(email)
            user_queryset = User.objects.filter(email=email)
            print(user_queryset)
            if queryset and user_queryset:
                category = Category.objects.filter(category_name=category_name)[0]
                owner = User.objects.filter(email=email)[0]
                product = Product.objects.create(product_name=product_name, product_description=product_description, product_price=product_price, product_category=category, owner=owner, image=image)
                return Response('Product OK')
            else:
                return Response('FAILED')


class CategoryView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request, format=None):
        categorys = Category.objects.all().values()
        return JsonResponse({"categorys":list(categorys)})
        #return Response('OK')
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            category_name = serializer.data.get('category_name')
            # check if user queryset exists 
            username = serializer.data.get('owner').get('username')
            email = serializer.data.get('owner').get('email')
            slug = serializer.data.get('owner').get('slug')

            queryset = User.objects.filter(email=email)
            owner = None
            if queryset:
                owner = User.objects.filter(email=email)[0]
                category = Category.objects.create(category_name = category_name, owner = owner)
                return Response('Category OK')
            else:
                return Response('FAILED')

class ProductUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProductUserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request, format=None):
        users = User.objects.all().values()
        return JsonResponse({"users": list(users)})
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            email = serializer.data.get('email')
            slug = serializer.data.get('slug')
            user = User.objects.create(username=username, email=email, slug = slug)
            
            return Response('User OK')
        
