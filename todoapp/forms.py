from .models import TodoItem
from django.forms import ModelForm
from django import forms

class AddItemForm(ModelForm):
	
	class Meta:
		model = TodoItem
		fields = ['content']
		widgets = { 'content': forms.TextInput(attrs={'size': 80,'placeholder':'Bir plan girin'})}