from django import forms

from .models import Health_Record


class MainForm(forms.ModelForm):
    class Meta:
        model = Health_Record
        # fields = '__all__'
        exclude = ('prediction', 'probability')

    def custom_save(self, user):
        lv = self.save(commit=False)
        lv.created_by = user
        lv.save()
        return lv

