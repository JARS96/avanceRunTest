from django.urls import path
from AppForms.views import create_curso, create_profesor, create_estudiante, search_alumno

urlpatterns =[
    path('create_curso', create_curso, name = 'create_curso'),
    path('create_profesor', create_profesor, name = 'create_profesor'),
    path('create_estudiante', create_estudiante, name = 'create_estudiante'),
    path('search_alumno', search_alumno, name = 'search_alumno'),
]