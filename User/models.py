from django.db import models
from Admin.models import *
from Guest.models import *
from Publisher.models import *

# Create your models here.

class tbl_uaddbook(models.Model):
    ubook_name=models.CharField(max_length=15)
    ubook_desc=models.CharField(max_length=50)
    ubook_price=models.IntegerField(default=0)
    ubook_photo=models.FileField(upload_to='Assets/UserBookPhoto/')
    ubook_authname=models.CharField(max_length=15)
    ubook_genre=models.ForeignKey(tbl_genre, on_delete=models.CASCADE)
    ubook_qlty=models.ForeignKey(tbl_quality, on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    ubook_status = models.IntegerField(default="0")

    
class tbl_swap(models.Model):
    swap_id=models.CharField(max_length=15)
    touser_id=models.ForeignKey(tbl_user, on_delete=models.CASCADE,related_name="touser_id")
    fromuser_id=models.ForeignKey(tbl_user, on_delete=models.CASCADE,related_name="fromuser_id")
    tobook_id=models.ForeignKey(tbl_uaddbook, on_delete=models.CASCADE,related_name="tobook_id")
    frombook_id=models.ForeignKey(tbl_uaddbook, on_delete=models.SET_NULL,related_name="frombook_id",null=True)
    swap_status=models.IntegerField(default=0)
    swap_price=models.CharField(max_length=15)
    swap_paymentstatus=models.IntegerField(default=0)
    agent = models.ForeignKey(tbl_agent,on_delete=models.CASCADE,null=True)

class tbl_booking(models.Model):
    booking_status = models.IntegerField(default=0)
    booking_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    booking_amount = models.CharField(max_length=30)
    agent = models.ForeignKey(tbl_agent,on_delete=models.SET_NULL,null=True)

class tbl_cart(models.Model):
    cart_qty = models.IntegerField(default=1)
    cart_status = models.IntegerField(default=0)
    product = models.ForeignKey(tbl_paddbook,on_delete=models.CASCADE)
    booking = models.ForeignKey(tbl_booking,on_delete=models.CASCADE)

class tbl_complaint(models.Model):
    complaint_id=models.CharField(max_length=15)
    complaint_title=models.CharField(max_length=50)
    complaint_desc=models.CharField(max_length=100)
    complaint_status=models.IntegerField(default=0)
    complaint_date=models.DateField(auto_now=True)
    complaint_reply=models.CharField(max_length=100,null=True)
    user_id=models.ForeignKey(tbl_user, on_delete=models.CASCADE,related_name="user_id",null=True)
    publisher_id=models.ForeignKey(tbl_publisher, on_delete=models.CASCADE,related_name="publisher_id",null=True)
    agent_id=models.ForeignKey(tbl_agent, on_delete=models.CASCADE,related_name="agent_id",null=True)

class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user_name=models.CharField(max_length=500)
    user_review=models.CharField(max_length=500)
    book=models.ForeignKey(tbl_paddbook,on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(tbl_user,on_delete=models.SET_NULL,null=True)
    datetime=models.DateTimeField(auto_now_add=True)


class tbl_usergenre(models.Model):
    genre=models.ForeignKey(tbl_genre,on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(tbl_user,on_delete=models.SET_NULL,null=True)

class tbl_wishlist(models.Model):
    book=models.ForeignKey(tbl_paddbook,on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(tbl_user,on_delete=models.SET_NULL,null=True)


class tbl_ubooking(models.Model):
    booking_status = models.IntegerField(default=0)
    booking_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    booking_amount = models.CharField(max_length=30)
    agent = models.ForeignKey(tbl_agent,on_delete=models.SET_NULL,null=True)

class tbl_ucart(models.Model):
    cart_qty = models.IntegerField(default=1)
    cart_status = models.IntegerField(default=0)
    product = models.ForeignKey(tbl_uaddbook,on_delete=models.CASCADE)
    booking = models.ForeignKey(tbl_ubooking,on_delete=models.CASCADE)

class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from")
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to")