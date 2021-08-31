from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Student

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

