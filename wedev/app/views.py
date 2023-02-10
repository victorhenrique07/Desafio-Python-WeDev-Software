from django.shortcuts import render
from django.http import HttpResponse
from app.forms import RegisterStaffForm

# Create your views here.

def home(request):
    return HttpResponse("Hi!")

def register_staff(request):
    context = {'form': RegisterStaffForm()}
    return render(request, 'index.html', context)