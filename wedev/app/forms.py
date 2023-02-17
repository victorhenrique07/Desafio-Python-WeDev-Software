from django import forms
from app.models import Curso, Infos, CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class TelefoneForm(forms.Form):

    class Meta:
        model = Infos
        
        fields = ['telefone']
        
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        
        fields = [
            'name',
            'start_date',
            'finish_date'
            ]