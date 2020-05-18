from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import*

class IdentiteCompleteForm(forms.ModelForm):
	slug  = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'slug'}))

	class Meta:
		model = IdentiteComplete
		# fields = ('quarter', 'attestionId', 'date')
		fields = ('slug','province', 'commune', 'zone', 'quarter', 'date')

	def __init__(self, *args, **kwargs):
		super(IdentiteCompleteForm, self).__init__(*args, **kwargs)

		self.fields['province'].widget.attrs['class'] = 'form-control'
		self.fields['province'].widget.attrs['placeholder'] = 'province'
		# self.fields['province'].label = ''


		self.fields['commune'].widget.attrs['class'] = 'form-control'
		self.fields['commune'].widget.attrs['placeholder'] = 'commune'
		# self.fields['commune'].label = ''


		self.fields['zone'].widget.attrs['class'] = 'form-control'
		self.fields['zone'].widget.attrs['placeholder'] = 'zone'
		# self.fields['zone'].label = ''


		self.fields['quarter'].widget.attrs['class'] = 'form-control'
		self.fields['quarter'].widget.attrs['placeholder'] = 'quarter'
		# self.fields['quarter'].label = ''


		# self.fields['attestionId'].widget.attrs['class'] = 'form-control'
		# self.fields['attestionId'].widget.attrs['placeholder'] = 'attestionId'
		# self.fields['attestionId'].label = ''



		self.fields['date'].widget.attrs['class'] = 'form-control'
		self.fields['date'].widget.attrs['placeholder'] = 'date'
		self.fields['date'].label = ''


