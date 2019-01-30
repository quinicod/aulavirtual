from django import forms

class Contacto(forms.Form):
    name=forms.CharField(label="Nombre Completo:", max_length=100, required=True)
    email=forms.EmailField(label="Email:", required=True)
    asunto=forms.CharField(label="Asunto:", max_length=150, required=True)
    mensaje=forms.CharField(label="Mensaje:", max_length=1000, required=True)