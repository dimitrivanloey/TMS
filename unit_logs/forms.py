from django import forms

from .models import Winx, Enable, Arkle, Denman, Kauto, Frankel, Entry, Enable_Entry, Arkle_Entry, Denman_Entry, Kauto_Entry, Frankel_Entry

class WinxForm(forms.ModelForm):
    class Meta:
        model = Winx
        fields = ['number', 'status']

class EnableForm(forms.ModelForm):
    class Meta:
        model = Enable
        fields = ['number', 'status']

class ArkleForm(forms.ModelForm):
    class Meta:
        model = Arkle
        fields = ['number', 'status']

class DenmanForm(forms.ModelForm):
    class Meta:
        model = Denman
        fields = ['number', 'status']

class KautoForm(forms.ModelForm):
    class Meta:
        model = Kauto
        fields = ['number', 'status']

class FrankelForm(forms.ModelForm):
    class Meta:
        model = Frankel
        fields = ['number', 'status']

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['status', 'venue', 'comments']

class EnableEntryForm(forms.ModelForm):
    class Meta:
        model = Enable_Entry
        fields = ['status', 'venue', 'comments']

class ArkleEntryForm(forms.ModelForm):
    class Meta:
        model = Arkle_Entry
        fields = ['status', 'venue', 'comments']

class DenmanEntryForm(forms.ModelForm):
    class Meta:
        model = Denman_Entry
        fields = ['status', 'venue', 'comments']

class KautoEntryForm(forms.ModelForm):
    class Meta:
        model = Kauto_Entry
        fields = ['status', 'venue', 'comments']

class FrankelEntryForm(forms.ModelForm):
    class Meta:
        model = Frankel_Entry
        fields = ['status', 'venue', 'comments']
