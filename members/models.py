from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=50, null=True,default=user.name)
    Last_name = models.CharField(max_length=50, null=True)
    Father_name = models.CharField(max_length=50, null=True)
    Mother_name = models.CharField(max_length=50, null=True)
    Address = models.CharField(max_length=200, null=True)
    roll_no = models.CharField(max_length=50, null=True)
    mobile_no = models.CharField(max_length=14, null=True)
    email = models.EmailField(max_length=50, null=True)
    DOB = models.DateField(null=True,)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('other','other'),
    )
    Gender = models.CharField(choices = GENDER_CHOICES ,max_length=6, null=True)
    image = models.ImageField(default='default.jpg',null=True,blank=True)
    date_created = models.DateField(auto_now_add=True, null=True)