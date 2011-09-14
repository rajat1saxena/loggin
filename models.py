from django.db import models
from django.contrib.auth.models import User
from django import forms

class userinfo(models.Model):
	country=models.CharField(max_length=30)
	age=models.IntegerField()
	user=models.OneToOneField(User) 

class SignupForm(forms.Form):
	username=forms.CharField(max_length=30)
	password=forms.CharField(max_length=50,widget=forms.PasswordInput)
	email=forms.EmailField()
	first_name=forms.CharField(max_length=30)
	last_name=forms.CharField(max_length=50)
	age=forms.IntegerField()
	country=forms.CharField(max_length=30)

