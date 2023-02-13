from django import forms
from app.models import Curso, Telefone, Informacao
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TelefoneForm(forms.Form):

    class Meta:
        model = Telefone
        
        fields = ['telefone']
        
        
class InformacoesForm(forms.ModelForm):
    
    class Meta:
        model = Informacao

        fields = '__all__'
        
        
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        
        fields = '__all__'