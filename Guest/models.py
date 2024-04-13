

# Create your models here.
from django.db import models
from Admin.models import *
# Create your models here.

class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    user_photo = models.FileField(upload_to='Assets/UserPhoto/')
    user_proof = models.FileField(upload_to='Assets/UserProof/')
    user_status = models.IntegerField(default="0")
    user_address = models.CharField(max_length=50,null=True)

class tbl_publisher(models.Model):
    publisher_name=models.CharField(max_length=15)
    publisher_contact=models.CharField(max_length=10)
    publisher_address=models.CharField(max_length=10)
    publisher_photo = models.FileField(upload_to='Assets/UserPhoto/')
    publisher_proof= models.FileField(upload_to='Assets/UserProof/')
    publisher_email=models.EmailField(max_length=50)
    publisher_password=models.CharField(max_length=10)
    user_status = models.IntegerField(default="0")

class tbl_agent(models.Model):
    agent_name=models.CharField(max_length=15)
    agent_contact=models.CharField(max_length=10)
    agent_address=models.CharField(max_length=10)
    agent_photo = models.FileField(upload_to='Assets/UserPhoto/')
    agent_proof= models.FileField(upload_to='Assets/UserProof/')
    agent_email=models.EmailField(max_length=50)
    agent_password=models.CharField(max_length=10)
    user_status = models.IntegerField(default="0")
    