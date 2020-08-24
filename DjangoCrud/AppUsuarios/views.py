from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import PersonaForm

def home(request):
    persona = Persona.objects.all()
    context = {'persona':persona}
    return render(request, 'home.html',context)

def listar(request):
    persona = Persona.objects.all()
    return render(request, 'dashboard.html', {'persona':persona})

def crear(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PersonaForm()
    return render(request,'usuario.html',{'form':form})

def editar(request, id):
    persona = Persona.objects.get(id = id)
    if request.method == 'GET':
        form = PersonaForm(instance = persona)
    else:
        form = PersonaForm(request.POST, instance = persona)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request,'usuario.html',{'form':form})

def eliminar(request,id):
    persona = Persona.objects.get(id = id)
    if request.method == 'POST':
        persona.delete()
        return redirect('listar')
    return render(request,'delete.html',{'persona':persona})

# Create your views here.
