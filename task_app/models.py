from django.db import models

# Create your models here.
#  name (charfield), description (textfield), and price (decimal field).

class Product(models.Model):
    name=models.CharField(max_length=50,default="",null=True,blank=True)
    descriptions=models.TextField(null=True,blank=True)
    price=models.FloatField(default="",null=True,blank=True)
   
    def __str__(self):
        return self.name

class MyUser(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20,default='general')
    password=models.CharField(max_length=500)
    def __str__(self):
        return self.firstname+"-"+self.lastname