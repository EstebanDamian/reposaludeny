from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput 



class crear_Numero_de_Turnos_forms(forms.Form):
    id_turno = forms.IntegerField(required=True)
    fecha = forms.DateField()
    hora = forms.TimeField()
    id_numero_de_consultorio = forms.ModelChoiceField(queryset=Consultorio.objects.all())
    id_sede = forms.ModelChoiceField(queryset=Sede_Clinica.objects.all())
    id_dni_paciente = forms.ModelChoiceField(queryset=Pacientes.objects.all())

class crear_Medico_forms(forms.Form):
    id_especialidad = forms.ModelChoiceField(queryset=Especialidad.objects.all())
    nombre_medico = forms.CharField(max_length=30)
    apellido_medico = forms.CharField(max_length=30)
    dni_medico = forms.IntegerField()
    id_matricula = forms.ModelChoiceField(queryset=Matricula.objects.all())
    id_numero_de_consultorio = forms.ModelChoiceField(queryset=Consultorio.objects.all())
    id_sede = forms.ModelChoiceField(queryset=Sede_Clinica.objects.all())

class crear_Matricula_forms(forms.Form):
    matricula= forms.IntegerField()
    numero_legajo = forms.IntegerField()
    años_de_servicio = forms.IntegerField(max_value=60)
    pacientes_atendidos = forms.IntegerField()


class crear_Especialidades_forms(forms.Form):
    
    nombre_especialidad=forms.CharField(max_length=30) 
      


class crear_Coberturas_forms(forms.Form):
    nombre_cobertura=forms.CharField()

    


class crear_Localidades_forms(forms.Form):
    localidad=forms.CharField(max_length=30)
    provincia=forms.CharField(max_length=30) 

class crear_Pacientes_forms(forms.Form):
    id_dni = forms.IntegerField()
    nombre_paciente = forms.CharField(max_length=30)
    apellido_paciente = forms.CharField(max_length=30)
    fecha_nacimiento = forms.DateField()
    sexo_paciente = forms.CharField(max_length=10)
    id_cobertura = forms.ModelChoiceField(queryset=Cobertura.objects.all())
    id_localidad = forms.ModelChoiceField(queryset=Localidad.objects.all())

class crear_Prepaga_forms(forms.Form):
    nombre_prepaga = forms.CharField(max_length=30)
    plan = forms.CharField(max_length=30)

class crear_Sede_forms(forms.Form):
    id_localidad = forms.ModelChoiceField(queryset=Localidad.objects.all())
    telefono_sede = forms.IntegerField()
    direccion_sede = forms.CharField()
    email_sede = forms.EmailField()

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    
    class Meta:
        model= User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        
        help_texts = {k:'' for k in fields}

class LoginForm(AuthenticationForm):
    username= forms.CharField(widget=TextInput())
    password= forms.CharField(widget=PasswordInput())
