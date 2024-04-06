from django.db import models

# Create your models here.

class tbl_district(models.Model):
    district_name=models.CharField(max_length=10)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=10)

class tbl_registration(models.Model):
    registration_name=models.CharField(max_length=15)
    registration_contact=models.CharField(max_length=10)
    registration_email=models.EmailField(max_length=50)
    registration_password=models.CharField(max_length=10)
'''
class tbl_publisher(models.Model):
    publisher_name=models.CharField(max_length=15)
    publisher_contact=models.CharField(max_length=10)
    publisher_email=models.EmailField(max_length=50)
    publisher_address=models.CharField(max_length=50)
'''
class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

    #models.CASCADE ===>fk del==>actual data del
    #models.SET_NULL,null=True

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_genre(models.Model):
    gen_name=models.CharField(max_length=20)

class tbl_quality(models.Model):
    quality_level=models.CharField(max_length=15)
    quality_rule=models.CharField(max_length=50)
    quality_percentage=models.CharField(max_length=15)

class tbl_admin(models.Model):
    admin_name = models.CharField(max_length=30)
    admin_contact = models.CharField(max_length=30)
    admin_email = models.CharField(max_length=30)
    admin_password = models.CharField(max_length=30)