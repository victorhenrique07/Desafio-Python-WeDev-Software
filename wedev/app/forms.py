from app.models import Aluno, Curso, EntidadeAssociativa, Professor, Telefone
from django import forms
from django.forms import inlineformset_factory


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno

        fields = ["name", "last_name", "email", "state", "city", "address"]


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor

        fields = ["name", "last_name", "email", "state", "city", "address"]


class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone

        fields = ["telefone"]


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso

        fields = ["name", "start_date", "finish_date"]


class EntidadeForm(forms.ModelForm):
    class Meta:
        model = EntidadeAssociativa

        fields = ["curso"]


TelefoneFormSetAluno = inlineformset_factory(
    Aluno, Telefone, form=TelefoneForm, extra=2
)
TelefoneFormSetProfessor = inlineformset_factory(
    Professor, Telefone, form=TelefoneForm, extra=2
)
CursoFormSet = inlineformset_factory(
    Aluno, EntidadeAssociativa, form=EntidadeForm, extra=2
)
