from django.db import models
from Admin.models import *

# Create your models here.

class tbl_paddbook(models.Model):
    pbook_name=models.CharField(max_length=15)
    pbook_desc=models.CharField(max_length=50)
    pbook_price=models.EmailField(max_length=50)
    pbook_photo=models.FileField(upload_to='Assets/PublisherAddBook/')
    pbook_authname=models.CharField(max_length=15)
    pbook_genre=models.ForeignKey(tbl_genre, on_delete=models.CASCADE)
    pbook_qty=models.CharField(max_length=15)
    