from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CursoForm, AlunoForm, ProfessorForm, TelefoneForm, TelefoneFormSetAluno, TelefoneFormSetProfessor, EditProfileForm
from django.contrib.auth.models import User
from .models import Telefone, Aluno, Professor
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def is_aluno(user):
    return user.groups.filter(name='aluno').exists()

def is_professor(user):
    return user.groups.filter(name='professor').exists()

@login_required(login_url='login')
@csrf_exempt
def updateuser(request, pk):
    user = request.user
    try:
        aluno = Aluno.objects.get(user=user)
        print(aluno)
        user_id = Aluno.objects.get(id=pk)
        form = AlunoForm(instance=user_id)
        telefone = TelefoneFormSetAluno(instance=user_id)
        if request.method == 'POST':
            form = AlunoForm(request.POST, instance=user_id)
            telefone = TelefoneFormSetAluno(request.POST, instance=user_id)
            if form.is_valid() and telefone.is_valid():
                form.save()
                telefone.save()
                print('deu certo')
                return redirect('/accounts/login')
        form = AlunoForm()
        telefone = TelefoneFormSetAluno()
        context = {
            'form': form,
            'telefone': telefone
        }
        return render(request, 'index.html', context)
        # usuário é um aluno
    except Aluno.DoesNotExist:
        try:
            professor = Professor.objects.get(user=user)
            print(professor)
            user_id = Professor.objects.get(id=pk)
            
            form = ProfessorForm(instance=user_id)
            telefone = TelefoneFormSetProfessor(instance=user_id)
            if request.method == 'POST':
                form = ProfessorForm(request.POST, instance=user_id)
                telefone = TelefoneFormSetProfessor(request.POST, instance=user_id)
                if form.is_valid() and telefone.is_valid():
                    form.save()
                    telefone.save()
                    print('deu certo')
                    return redirect('/accounts/login')
            form = ProfessorForm()
            telefone = TelefoneFormSetProfessor()
            context = {
                'form': form,
                'telefone': telefone
            }
            return render(request, 'index.html', context)
                # usuário é um professor
        except Professor.DoesNotExist:
            return HttpResponse("ERROR")
            # usuário não é um aluno nem professor
    

@login_required(login_url='login')
def teste(request):
    pessoa = request.user
    telefone = Telefone.objects.get(id=2)
    if telefone is None:
        print('Usuario não tem telefone.')
    print(pessoa.id)
    context = {
        'form': pessoa,
    }
    return render(request, 'cursos_usuario.html', context)

@login_required
def student_course(request):
    return render(request, "index.html", {'form': AlunoForm()})