from sqlite3 import Timestamp
from django.shortcuts import render
from AppForms.models import Curso, Profesor, Estudiante
from AppForms.forms import Curso_form, Profesor_form, Estudiante_form

def create_curso(request):
      
      if request.method == 'GET':
            cursos = Curso_form ()
            context = {'cursos':cursos}
            return render(request,'create_curso.html', context=context)
      else:
            cursos = Curso_form(request.POST)
            if cursos.is_valid():
                  new_curso = Curso.objects.create(
                        nombre = cursos.cleaned_data['nombre'],
                        camada = cursos.cleaned_data['camada'],
                  )
            context = {'new_curso':new_curso}
            return render(request,'create_curso.html', context = context)


def create_profesor(request):
      
      if request.method == 'GET':
            profesores = Profesor_form ()
            context = {'profesores':profesores}
            return render(request,'create_profesor.html', context=context)
      else:
            profesores = Profesor_form(request.POST)
            if profesores.is_valid():
                  new_profesor = Profesor.objects.create(
                        nombre = profesores.cleaned_data['nombre'],
                        apellido = profesores.cleaned_data['apellido'],
                        email = profesores.cleaned_data['email'],
                        profesion = profesores.cleaned_data['profesion'],
                  )
            context = {'new_profesor':new_profesor}
            return render(request,'create_profesor.html', context=context)  


def create_estudiante(request):
      
      if request.method == 'GET':
            estudiantes = Estudiante_form ()
            context = {'estudiantes':estudiantes}
            return render(request,'create_estudiante.html', context=context)
      else:
            estudiantes = Estudiante_form(request.POST)
            if estudiantes.is_valid():
                  new_estudiante = Estudiante.objects.create(
                        legajo = estudiantes.cleaned_data['legajo'],
                        nombre = estudiantes.cleaned_data['nombre'],
                        apellido = estudiantes.cleaned_data['apellido'],
                        email = estudiantes.cleaned_data['email'],
                  )
            context = {'new_estudiante':new_estudiante}
            return render(request,'create_estudiante.html', context=context)                   

def search_alumno(request):
    print(request.GET)
    estudiantes = Estudiante.objects.filter(nombre__contains = request.GET['search'])
    context = {'estudiantes':estudiantes}
    return render(request, 'search_alumno.html', context = context)
   