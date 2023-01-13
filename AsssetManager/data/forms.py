from django import forms 
from .models import Asset,EmployeeAsset
from django.forms import TextInput, Select, FileInput, NumberInput, Textarea,DateInput



class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Asset'}),
            'specifications': TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Specification'}),
            'condition': Select(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Condition'}),
            'location': TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Location'}),
            'date_entered': DateInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'date', 'type':'date'}),
            
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeAsset
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Asset'}),
            'specifications': TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Specification'}),
            'condition': Select(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Condition'}),
            'location': TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Location'}),
            'date_entered': DateInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'date', 'type':'date'}),
            
        }

