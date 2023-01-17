from dataclasses import field, fields
# from socket import fromshare
from django import forms
from . import models

class MyUserForms(forms.ModelForm):
    firstname=forms.CharField(max_length=20,label="First Name       ")
    lastname=forms.CharField(max_length=20,label="Last Name     ")
    username=forms.CharField(max_length=20,label="User Name     ")
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = models.MyUser
        fields = {'firstname','lastname','username','password'}