from django.views.generic.edit import FormView
from .models import Seccion
from .forms import Contacto
from django import forms

class Contacta(FormView):
    template_name="aula/contacta.html"
    form_class = Contacto
    
    def get_form(self, form_class=None):
        form=super(Contacta,self).get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'form-control mb2','placeholder':'Nombre Completo'})
        form.fields['email'].widget=forms.EmailInput(attrs={'class':'form-control mb2','placeholder':'Email'})
        form.fields['asunto'].widget=forms.TextInput(attrs={'class':'form-control mb2','placeholder':'Asunto'})
        form.fields['mensaje'].widget=forms.Textarea(attrs={'class':'form-control mb2','placeholder':'Mensaje'})

        return form
