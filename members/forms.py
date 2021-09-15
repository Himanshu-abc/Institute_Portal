from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import *

class createuserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class studentForm(ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['user',]
        widgets = {
            'DOB': forms.SelectDateWidget,
        }

class Image_galleryForm(ModelForm):

    class Meta:
        model = Image_gallery
        fields = '__all__'

class News_galleryForm(ModelForm):

    class Meta:
        model = News_gallery
        fields = '__all__'

class Event_updatesForm(ModelForm):

    class Meta:
        model = Upcoming_event
        fields = '__all__'
        widgets = {
            'event_start_date' : forms.SelectDateWidget,
            'event_end_date' : forms.SelectDateWidget,
        }
