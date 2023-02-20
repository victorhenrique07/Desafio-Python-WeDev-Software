from django import forms
from django.forms import inlineformset_factory
from app.models import Curso, Aluno, Professor, Telefone
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        
        fields = ['name', 'last_name', 'email', 'state', 'city', 'address']
        
class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        
        fields = ['name', 'last_name', 'email', 'state', 'city', 'address']
        
class TelefoneForm(forms.ModelForm):

    class Meta:
        model = Telefone
        
        fields = ['telefone']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        
        fields = [
            'name',
            'start_date',
            'finish_date'
            ]
        
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
        
TelefoneFormSetAluno = inlineformset_factory(Aluno, Telefone, form=TelefoneForm, extra=2)
TelefoneFormSetProfessor = inlineformset_factory(Professor, Telefone, form=TelefoneForm, extra=2)