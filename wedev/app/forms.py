from django import forms
from app.models import Curso, Aluno, Professor



class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        
        fields = ['name', 'last_name', 'email', 'state', 'city', 'address']
        
class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        
        exclude = ['user']
        
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        
        fields = [
            'name',
            'start_date',
            'finish_date'
            ]