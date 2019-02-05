from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm


class nuevoPostForm(forms.Form):
    descripcion=forms.CharField(label='Descripción', required=True, max_length=500, widget=forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Escribe tu pregunta...'}))

class nuevaRespuestaForm(forms.Form):
    respuesta=forms.CharField(label='Respuesta', required=True, max_length=500, widget=forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Escribe tu respuesta...'}))



