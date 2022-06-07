from django import forms
from AppForms.models import Curso, Estudiante, Profesor

class Curso_form (forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class Estudiante_form (forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class Profesor_form (forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

