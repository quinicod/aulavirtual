from django import forms
from noticias.models import Noticia


class NoticiasForm(forms.ModelForm):
    class Meta:
        model=Noticia
        fields=['titulo','contenido','imagen']
        widgets={
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'contenido': forms.Textarea(attrs={'class':'form-control'}),
            'imagen': forms.FileInput(attrs={'class':'form-control-file', 'required':'true'}),
        }
