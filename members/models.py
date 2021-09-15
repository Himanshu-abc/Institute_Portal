from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Student(models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=50, null=True)
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
    image = models.ImageField(default='profile/default.jpg',null=True,blank=True,upload_to='profile/')
    date_created = models.DateField(auto_now_add=True, null=True)

class Image_gallery(models.Model):

    def __str__(self):
        return self.images.name

    images = models.ImageField(default='image_gallery/default.jpg', upload_to='image_gallery/', null=True, blank=True)

class Upcoming_event(models.Model):

    def __str__(self):
        return self.event_name

    event_name = models.CharField(max_length=50, null=True)
    event_start_date = models.DateField(null=True)
    event_end_date = models.DateField(null=True)
    event_description = models.CharField(max_length=50, null=True)

class News_gallery(models.Model):

    def __str__(self):
        return self.news_title or self.news_pdf.name

    news_title = models.CharField(max_length=50, blank=False, null=True)
    news_pdf = models.FileField(default='news_pdf/Appraisal.pdf',null=True, blank=True, upload_to='news_pdf/')
