from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.

class tbl_uaddbook(models.Model):
    ubook_name=models.CharField(max_length=15)
    ubook_desc=models.CharField(max_length=50)
    ubook_price=models.EmailField(max_length=50)
    ubook_photo=models.FileField(upload_to='Assets/UserBookPhoto/')
    ubook_authname=models.CharField(max_length=15)
    ubook_genre=models.ForeignKey(tbl_genre, on_delete=models.CASCADE)
    ubook_qlty=models.ForeignKey(tbl_quality, on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    
class tbl_swap(models.Model):
    swap_id=models.CharField(max_length=15)
    touser_id=models.ForeignKey(tbl_user, on_delete=models.CASCADE,related_name="touser_id")
    fromuser_id=models.ForeignKey(tbl_user, on_delete=models.CASCADE,related_name="fromuser_id")
    tobook_id=models.ForeignKey(tbl_uaddbook, on_delete=models.CASCADE,related_name="tobook_id")
    frombook_id=models.ForeignKey(tbl_uaddbook, on_delete=models.SET_NULL,related_name="frombook_id",null=True)
    swap_status=models.CharField(max_length=15)
    swap_price=models.CharField(max_length=15)
    swap_paymentstatus=models.CharField(max_length=15)
