from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def buscar(request):
    return render(request, 'search_alumno.html')