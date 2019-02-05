from django import forms
from .models import File_Evento,Seccion, File_seccion
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class Contacto(forms.Form):
    name=forms.CharField(label="Nombre Completo:", max_length=100, required=True)
    email=forms.EmailField(label="Email:", required=True)
    asunto=forms.CharField(label="Asunto:", max_length=150, required=True)
    mensaje=forms.CharField(label="Mensaje:", max_length=1000, required=True)

class nuevaSeccion(forms.ModelForm):
    class Meta:
        model=Seccion
        fields= ['titulo']

class anyadirMaterial(forms.ModelForm):
    class Meta:
        model=File_seccion
        fields= ['file','descripcion']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = File_seccion
        fields= ['descripcion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Actualizar'))

class EventoForm(forms.ModelForm):
    class Meta:
        model = File_Evento
        fields = ['file']
        labels=[
            'file:Archivos'
        ]