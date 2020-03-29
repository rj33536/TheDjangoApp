from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=5000)
    long_description=models.CharField(max_length=999999 ,default='No information')
    price=models.FloatField()
    image=models.ImageField(upload_to="photos/")
    cart = models.ManyToManyField(User, related_name="cart")
class order(models.Model):
    myproduct=models.IntegerField(default=1)
    name=models.CharField(max_length=20)
    Mobile=models.BigIntegerField()
    Address=models.CharField(max_length=500, default='shastri park')
    email=models.EmailField(default="rj33536@gmail.com")