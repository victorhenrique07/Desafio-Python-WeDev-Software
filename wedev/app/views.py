from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import StaffForm

# Create your views here.

def home(request):
    return HttpResponse("Hi!")

def register_staff(request):
    form = StaffForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/app')
    context = {'form': StaffForm()}
    return render(request, 'index.html', context)