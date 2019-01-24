from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm
from aula.models import Seccion, File_seccion

class nuevoPostForm(forms.Form):
    descripcion=forms.CharField(label='Descripción', required=True, max_length=500, widget=forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Escribe tu pregunta...'}))

class nuevaRespuestaForm(forms.Form):
    respuesta=forms.CharField(label='Respuesta', required=True, max_length=500, widget=forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Escribe tu respuesta...'}))

class nuevaSeccion(ModelForm):
    class Meta:
        model=Seccion
        fields= ['titulo']

class anyadirMaterial(ModelForm):
    class Meta:
        model=File_seccion
        fields= ['file','descripcion']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = File_seccion
        fields= ['file','descripcion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Actualizar'))

