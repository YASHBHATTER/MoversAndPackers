from operator import truediv
from turtle import title
from urllib import request
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SiteUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15,null=True)
    location = models.CharField(max_length=200,null=True)
    shiftinglocation = models.CharField(max_length=200,null=True)
    briefitems = models.CharField(max_length=100,null=True)
    items = models.CharField(max_length=3000,null=True)
    professional = models.CharField(max_length=200,null=True)
    requestdate = models.DateField(null=True)
    remark = models.CharField(max_length=500,null=True)
    status = models.CharField(max_length=30,null=True)
    updationdate = models.DateField(null=True)

    def __str__(self):
        return self.user.username

class Services(models.Model):
    title = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=5000,null=True)
    image = models.FileField(null=True)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=10,null=True)
    emailid = models.CharField(max_length=100,null=True)
    subject = models.CharField(max_length=100,null=True)
    message = models.CharField(max_length=10,null=True)
    mdate = models.DateField(null=True)
    isread = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.name