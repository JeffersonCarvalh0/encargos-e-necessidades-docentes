from django import forms
from crud.models import Campus

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = '__all__'
