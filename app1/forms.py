from django import forms
from .models import blogform3

class blogform2(forms.ModelForm):
	class Meta:
		model=blogform3
		fields=['First_Name','Middle_Name','Last_Name',]