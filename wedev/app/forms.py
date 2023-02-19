from django import forms
from app.models import Curso, Infos, CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from crispy_forms.helper import FormHelper



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        exclude = ['user_permissions', 'is_staff', 'is_active', 'is_superuser', 'last_login',
                   'groups', 'type', 'password', 'date_joined']
        
        
class CustomUserPainel(forms.ModelForm):
    class Meta:
        model = CustomUser
        
        exclude = ['user_permissions', 'is_staff', 'is_active', 'is_superuser', 'last_login',
                   'groups', 'type', 'password', 'date_joined']
        
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