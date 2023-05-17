from django.db import models
from django.contrib.auth.models import User

class ProductUser(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.username

class Category(models.Model):
    category_name = models.CharField(max_length=250)
    owner = models.ForeignKey(ProductUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_description = models.CharField(max_length=1000)
    product_price = models.IntegerField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    

