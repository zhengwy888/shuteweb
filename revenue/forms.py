from django.db import models
from django import forms
from django.forms import ModelForm, extras
from revenue.models import Transaction
import datetime

class AddTransForm(ModelForm):
    date = forms.DateField(widget=extras.SelectDateWidget)
    class Meta:
        model = Transaction
        fields = ['date', 'type', 'amount']
