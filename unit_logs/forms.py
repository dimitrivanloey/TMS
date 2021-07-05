from django import forms

from .models import *

class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ['group', 'number', 'status', 'start_date']

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['tracker', 'status', 'venue', 'comments']

class TrackerFailureForm(forms.ModelForm):
    class Meta:
        model = Failure
        fields = ['tracker', 'code', 'start_date', 'end_date']
