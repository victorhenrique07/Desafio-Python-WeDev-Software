from django import forms
from app.models import Curso, Telefone, Aluno, Professor
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TelefoneForm(forms.Form):

    class Meta:
        model = Telefone
        
        fields = ['telefone']
        
        
class AlunoForm(forms.ModelForm):
    
    class Meta:
        model = Aluno

        fields = '__all__'
        
class ProfessorForm(forms.ModelForm):
    
    class Meta:
        model = Professor

        fields = '__all__'
        
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        
        fields = '__all__'