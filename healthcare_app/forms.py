from django import forms

from .models import Health_Record


class MainForm(forms.ModelForm):
    class Meta:
        model = Health_Record
        fields = '__all__'

