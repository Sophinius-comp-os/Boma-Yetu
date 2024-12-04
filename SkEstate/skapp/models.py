from django.db import models
from django.db.models import  Model

# Create your models here.
class Tenant(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    yob = models.DateField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname
class House_detail(models.Model):
    name = models.CharField(max_length=200)
    area = models.IntegerField()
    beds = models.IntegerField(max_length=200)
    baths = models.IntegerField(max_length=20)
    garages = models.IntegerField(max_length=20)

    def __str__(self):
        return self.name


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    date = models.DateTimeField()
    offer = models.CharField(max_length=50)
    agent = models.CharField(max_length=50)
    message = models.TextField()


def __str__(self):
    return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()


    def __str__(self):
      return  f"Message from {self.name}"

class Agent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class User(models.Model):
   name = models.CharField(max_length=50)
   username = models.CharField(max_length=50)
   password = models.CharField(max_length=50)

   def __str__(self):
       return self.name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title