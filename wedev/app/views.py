from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .forms import (
    AlunoForm,
    CursoFormSet,
    ProfessorForm,
    TelefoneFormSetAluno,
    TelefoneFormSetProfessor,
    CursoForm,
)
from .models import Aluno, Professor, Telefone, Curso, EntidadeAssociativa

# Create your views here.


@login_required(login_url="login")
@permission_required("app.editar_perfil")
def updateuser(request, pk):
    user = request.user
    try:
        aluno = Aluno.objects.get(user=user)
        print(aluno)
        user_id = Aluno.objects.get(id=pk)
        form = AlunoForm(instance=user_id)
        telefone = TelefoneFormSetAluno(instance=user_id)
        curso = CursoFormSet(instance=user_id)
        if request.method == "POST":
            form = AlunoForm(request.POST, instance=user_id)
            telefone = TelefoneFormSetAluno(request.POST, instance=user_id)
            curso = CursoFormSet(request.POST, instance=user_id)
            if form.is_valid() and telefone.is_valid() and curso.is_valid():
                form.save()
                telefone.save()
                curso.save()
                print("deu certo")
                return redirect("/accounts/login")
        form = AlunoForm()
        telefone = TelefoneFormSetAluno()
        curso = CursoFormSet()
        context = {"form": form, "telefone": telefone, "curso": curso}
        return render(request, "index.html", context)
        # usuário é um aluno
    except Aluno.DoesNotExist:
        try:
            professor = Professor.objects.get(user=user)
            print(professor)
            user_id = Professor.objects.get(id=pk)

            form = ProfessorForm(instance=user_id)
            telefone = TelefoneFormSetProfessor(instance=user_id)
            if request.method == "POST":
                form = ProfessorForm(request.POST, instance=user_id)
                telefone = TelefoneFormSetProfessor(request.POST, instance=user_id)
                if form.is_valid() and telefone.is_valid():
                    form.save()
                    telefone.save()
                    print("deu certo")
                    return redirect("/accounts/login")
            form = ProfessorForm()
            telefone = TelefoneFormSetProfessor()
            context = {"form": form, "telefone": telefone}
            return render(request, "index.html", context)
            # usuário é um professor
        except Professor.DoesNotExist:
            return HttpResponse("ERROR")
            # usuário não é um aluno nem professor


@login_required(login_url="login")
def viewprofile(request, pk):
    form = Aluno.objects.get(id=pk)
    enti = EntidadeAssociativa.objects.get(id=pk)
    curso = Curso.objects.get(id=enti.curso_id)
    context = {"form": form, "curso": curso}
    return render(request, "cursos_usuario.html", context)


@login_required(login_url="login")
@permission_required("app.view_aluno")
def viewalunos(request):
    aluno = Aluno.objects.all()
    context = {"alunos": aluno}
    return render(request, "alunos.html", context)


@login_required(login_url="login")
@permission_required("app.view_curso")
def viewcursos(request):
    curso = Curso.objects.all()
    context = {"cursos": curso}
    return render(request, "cursos.html", context)
