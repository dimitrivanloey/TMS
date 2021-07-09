from django import forms

from .models import *

class StatusChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.category} - {obj.description}"

class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ['tracker_group', 'number']

class EntryForm(forms.ModelForm):
    status = StatusChoiceField(queryset=Status.objects.all().order_by('category'))

    class Meta:
        model = Entry
        fields = ['tracker', 'status', 'timestamp', 'venue', 'comments']
