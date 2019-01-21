from django import forms

class nuevoPostForm(forms.Form):
    descripcion=forms.CharField(label='Descripción', required=True, max_length=500, widget=forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Escribe tu pregunta...'}))

class nuevaRespuestaForm(forms.Form):
    respuesta=forms.CharField(label='Respuesta', required=True, max_length=500, widget=forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Escribe tu respuesta...'}))
