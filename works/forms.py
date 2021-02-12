from django import forms
from django.forms import ModelForm
from .models import *


# My View creation

class TaskForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    
    class Meta: 
        model = Works 
        fields = '__all__'

