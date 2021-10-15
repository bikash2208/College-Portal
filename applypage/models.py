from django.db import models


# Create your models here.
class student(models.Model):
    application_id=models.CharField(max_length=10)
    name=models.CharField(max_length=30)
    ftname=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    dob=models.CharField(max_length=12)
    mob=models.CharField(max_length=15)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    pincode=models.CharField(max_length=10)
    edu=models.CharField(max_length=10) 
    college_name=models.CharField(max_length=30)
    board=models.CharField(max_length=30)
    percentage=models.CharField(max_length=10)
    pic=models.FileField(max_length=50)
    sign=models.FileField(max_length=50)
    applieddate=models.CharField(max_length=12)
    approve_status=models.CharField(max_length=10)
