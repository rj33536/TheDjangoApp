from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=5000)
    long_description=models.CharField(max_length=999999 ,default='No information')
    price=models.FloatField()
    image=models.ImageField(upload_to="photos/")
    