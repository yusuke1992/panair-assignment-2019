from django import forms
from django.forms import DateInput
from .models import User, Record

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name', 'gender', 'age')

class RecordForm(forms.ModelForm):

    class Meta:
        model   = Record
        fields  = ('user', 'curriculum', 'date', 'time')
        widgets = {
            'date' : DateInput(attrs = { "type": "date" })
        }
