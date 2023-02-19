from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CursoForm, CustomUserChangeForm, CustomUserPainel
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
       form = CustomUserChangeForm(request.POST, instance=request.user)
       if form.is_valid():
           form.save()
           messages.success(request, "Deu certo")
           return redirect('/app')
    form = CustomUserChangeForm()
    context = {
        'form': form,
        'user': request.user
    }
    return render(request, "index.html", context)

@login_required
def student_course(request):
    return render(request, "index.html", {'form': CustomUserPainel()})