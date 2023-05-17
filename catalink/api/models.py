from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.conf import settings

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    slug = models.SlugField(default="", null=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['slug']
    def __str__(self):
        return self.username

class Category(models.Model):
    category_name = models.CharField(max_length=250)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_description = models.CharField(max_length=1000)
    product_price = models.IntegerField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productImages', blank=True, null=True)

    def __str__(self):
        return self.product_name
    

