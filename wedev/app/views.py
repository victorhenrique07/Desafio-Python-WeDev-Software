from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CursoForm, AlunoForm, ProfessorForm
from django.contrib.auth.models import User
from .models import Telefone, Aluno, Professor
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required(login_url='login')
@csrf_exempt
def updateuser(request, pk):
    user_id = Aluno.objects.get(id=pk)
    form = AlunoForm(instance=teste)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=user_id)
        if form.is_valid():
            form.save()
            print('deu certo')
            return redirect('/accounts/login')
        
    form = AlunoForm()
    context = {
        'form': form
    }    
    return render(request, "index.html", context)

@login_required(login_url='login')
def teste(request):
    pessoa = request.user
    telefone = Telefone.objects.get(id=2)
    if telefone is None:
        print('Usuario não tem telefone.')
    print(pessoa.id)
    context = {
        'form': pessoa
    }
    return render(request, 'cursos_usuario.html', context)

@login_required
def student_course(request):
    return render(request, "index.html", {'form': AlunoForm()})