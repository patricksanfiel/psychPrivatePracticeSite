from django import forms
from django.forms import ModelForm, DateTimeField
from .models import Client
from datetimepicker.widgets import DateTimePicker


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name','last_name','email','phone','appointment_date','therapist']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={ 'id':'date', 'class':'date', 'input_formats':["%m/%d/%Y h:mm TT"]}),
        }
