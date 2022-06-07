from dataclasses import fields
from django import forms
from cliente.models import DatosPersonales,Dispositivo


class FormDatos(forms.ModelForm):
        
    class Meta:
        model = DatosPersonales

        fields = '__all__'
        
        widgets = {
            'numero': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.Textarea(attrs={'class':'form-control'}),
            'num_serie': forms.Select(attrs={'class':'form-control'}),
            
        }
        
class FormDispositivo(forms.ModelForm):
        
    class Meta:
        model = Dispositivo

        fields = '__all__'
        
        widgets = {
            'tipo': forms.Select(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'modelo': forms.TextInput(attrs={'class':'form-control'}),
            'num_serie': forms.TextInput(attrs={'class':'form-control'}),
            'accesorios': forms.TextInput(attrs={'class':'form-control'}),
            'contra': forms.TextInput(attrs={'class':'form-control'}),
            'falla': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            'extras': forms.Textarea(attrs={'class':'form-control'}),
        }
