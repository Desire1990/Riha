from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import*

class IdentiteCompleteForm(forms.ModelForm):

    class Meta:
        model = IdentiteComplete
        fields = '__all__'


