from django import forms
from app.models import Usuario, Curso, Telefone, Aluno


class TelefoneForm(forms.Form):

    class Meta:
        model = Telefone
        
        fields = ['telefone']
        
        
class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario

        fields = '__all__'
        
        
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        
        fields = '__all__'


class AlunoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Aluno
        
        fields = '__all__'