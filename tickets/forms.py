from django import forms 
from .models import especialidadTI, soporteTI, tickets

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model= especialidadTI
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }

class SoporteForm(forms.ModelForm):
    class Meta:
        model= soporteTI
        fields = ['nombre', 'imagen','especialidad']
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'imagen' : forms.FileInput(attrs={'class':'form-control'}),
            'especialidad' : forms.SelectMultiple(attrs={'class':'form-control'}),
        }

class TicketsForm(forms.ModelForm):
    class Meta:
        model= tickets
        fields = ['titulo', 'descripcion', 'soporte']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control'}),
            'soporte' : forms.Select(attrs={'class':'form-control'}),
        }
