from django.shortcuts import render
from AppSalud.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm

def mostrar_index(request):
    
    return render (request, 'AppSalud/index.html')



def mostrar_Numero_de_Turno(request):
    numero_de_turno = Numero_de_Turno.objects.all()

    context = {'numero_de_turno': numero_de_turno}

    return render(request, 'AppSalud/numero_de_turno.html', context=context)

def crear_Numero_de_Turno(request):
    if request.method == 'POST':
        form=crear_Numero_de_Turnos_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            turnos = Numero_de_Turno(id_turno=formulario_limpio['id_turno'], fecha=formulario_limpio['fecha'], hora=formulario_limpio['hora'], id_numero_de_consultorio=formulario_limpio['id_numero_de_consultorio'], id_sede=formulario_limpio['id_sede'], id_dni_paciente=formulario_limpio['id_dni_paciente'])

            turnos.save()

            return render(request, 'AppSalud/index.html')
        
    
    else:
        form = crear_Numero_de_Turnos_forms()

    return render(request, 'AppSalud/crear_numero_de_turno.html', {'form': form})





def buscar_Numero_de_Turno(request):
    if request.GET.get('id_turno', False):
        id_turno = request.GET['id_turno']
        turno = Numero_de_Turno.objects.filter(id_turno__icontains=id_turno)

        return render(request, 'AppSalud/buscar_numero_de_turno.html', {'turnos': turno})
    else:
        respuesta = 'No se encuentra el N° de Turno'
    
    return render(request, 'AppSalud/buscar_numero_de_turno.html', {'respuesta': respuesta})

def actualizar_Numero_de_Turno(request, turno_id):
    turno = Numero_de_Turno.objects.get(id_turno=turno_id)
    if request.method == 'POST':
        form = crear_Numero_de_Turnos_forms(request.POST)

        if form.is_valid():

            formulario_limpio = form.cleaned_data

            turno.id_turno = formulario_limpio['id_turno']
            turno.fecha = formulario_limpio['fecha']
            turno.hora = formulario_limpio['hora']
            turno.id_numero_de_consultorio = formulario_limpio['id_numero_de_consultorio']
            turno.id_sede = formulario_limpio['id_sede']
            turno.id_dni_paciente = formulario_limpio['id_dni_paciente']

            turno.save()

            return render(request, 'AppSalud/index.html')
    
    else:
        form = crear_Numero_de_Turnos_forms(initial={'id_turno': turno.id_turno, 'fecha': turno.fecha, 'hora': turno.hora, 'id_numero_de_consultorio': turno.id_numero_de_consultorio, 'id_sede': turno.id_sede, 'id_dni_paciente': turno.id_dni_paciente})
    
    return render(request, 'AppSalud/actualizar_numero_de_turno.html', {'form': form})

def eliminar_numero_de_turno(request, turno_id):
    turno = Numero_de_Turno.objects.get(id_turno=turno_id)
    turno.delete()

    turno = turno.objects.all()

    context = {'turno': turno}

    return render(request, 'AppSalud/index.html',context=context)

def mostrar_medicos(request):
    medicos = Medicos.objects.all()

    context = {'medicos': medicos}

    return render(request, 'AppSalud/medicos.html', context=context)

def crear_Medico(request):
    if request.method == 'POST':
        form=crear_Medico_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            medicos = Medicos(id_especialidad=formulario_limpio['id_especialidad'], nombre_medico=formulario_limpio['nombre_medico'], apellido_medico=formulario_limpio['apellido_medico'], dni_medico=formulario_limpio['dni_medico'], id_matricula=formulario_limpio['id_matricula'], id_numero_de_consultorio=formulario_limpio['id_numero_de_consultorio'], id_sede=formulario_limpio['id_sede'] )

            medicos.save()

            return render(request, 'AppSalud/index.html')
    
    else:
        form = crear_Medico_forms()

    return render(request, 'AppSalud/crear_medico.html', {'form': crear_Medico_forms})

def buscar_nombre_medico(request):
    if request.GET.get('nombre_medico', False):
        nombre_medico = request.GET['nombre_medico']
        medico = Medicos.objects.filter(nombre_medico__icontains=nombre_medico)

        return render(request, 'AppSalud/buscar_nombre_medico.html', {'medicos': medico})
    else:
        respuesta = 'No se encuentra el Nombre del Medico'
    
    return render(request, 'AppSalud/buscar_nombre_medico.html', {'respuesta': respuesta})

def actualizar_Medico(request, medico_id):
    medico = Medicos.objects.get(id=medico_id)
    if request.method == 'POST':
        form = crear_Medico_forms(request.POST)

        if form.is_valid():

            formulario_limpio = form.cleaned_data

            
            medico.id_especialidad = formulario_limpio['id_especialidad']
            medico.nombre_medico = formulario_limpio['nombre_medico']
            medico.apellido_medico = formulario_limpio['apellido_medico']
            medico.dni_medico = formulario_limpio['dni_medico']
            medico.id_matricula = formulario_limpio['id_matricula']
            medico.id_numero_de_consultorio = formulario_limpio['id_numero_de_consultorio']
            medico.id_sede = formulario_limpio['id_sede']

            medico.save()

            return render(request, 'AppSalud/index.html')
    
    else:
        form = crear_Medico_forms(initial={'id_especialidad': medico.id_especialidad, 'nombre_medico': medico.nombre_medico, 'apellido_medico': medico.apellido_medico, 'dni_medico': medico.dni_medico, 'id_matricula': medico.id_matricula, 'id_numero_de_consultorio': medico.id_numero_de_consultorio, 'id_sede': medico.id_sede})
    
    return render(request, 'AppSalud/actualizar_medico.html', {'form': form})

def eliminar_medico(request, medico_id):
    medico = Medicos.objects.get(id=medico_id)
    medico.delete()

    medico = medico.objects.all()

    context = {'medico': medico}

    return render(request, 'AppSalud/index.html',context=context)

def mostrar_matricula(request):
    matricula = Matricula.objects.all()

    context = {'matricula': matricula}

    return render(request, 'AppSalud/matricula.html', context=context)

def crear_Matricula(request):
    if request.method == 'POST':
        form=crear_Matricula_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            matricula = Matricula(matricula=formulario_limpio['matricula'], numero_legajo=formulario_limpio['numero_legajo'], años_de_servicio=formulario_limpio['años_de_servicio'], pacientes_atendidos=formulario_limpio['pacientes_atendidos'])

            matricula.save()

            return render(request, 'AppSalud/index.html')
    
    else:
        form = crear_Matricula_forms()

    return render(request, 'AppSalud/crear_matricula.html', {'form': crear_Matricula_forms})

def buscar_numero_matricula(request):
    if request.GET.get('matricula', False):
        matricula = request.GET['matricula']
        matri = Matricula.objects.filter(matricula__icontains=matricula)
    
        return render(request, 'AppSalud/buscar_numero_matricula.html', {'matriculas': matri})
    else:
        respuesta = 'No se encuentra el Numero de Matricula'
    
    return render(request, 'AppSalud/buscar_numero_matricula.html', {'respuesta': respuesta})

def buscar_nombre_medico(request):
    if request.GET.get('nombre_medico', False):
        nombre_medico = request.GET['nombre_medico']
        medico = Medicos.objects.filter(nombre_medico__icontains=nombre_medico)

        return render(request, 'AppSalud/buscar_nombre_medico.html', {'medicos': medico})
    else:
        respuesta = 'No se encuentra el Nombre del Medico'
    
    return render(request, 'AppSalud/buscar_nombre_medico.html', {'respuesta': respuesta})

def actualizar_Matricula(request, matricula_id):
    matricul = Matricula.objects.get(matricula=matricula_id)
    if request.method == 'POST':
        form = crear_Matricula_forms(request.POST)

        if form.is_valid():

            formulario_limpio = form.cleaned_data

            matricul.matricula= formulario_limpio['matricula']
            matricul.numero_legajo = formulario_limpio['numero_legajo']
            matricul.años_de_servicio = formulario_limpio['años_de_servicio']
            matricul.pacientes_atendidos = formulario_limpio['pacientes_atendidos']
            matricul.save()

            return render(request, 'AppSalud/index.html')
    
    else:
        form = crear_Matricula_forms(initial={'matricula': matricul.matricula, 'numero_legajo': matricul.numero_legajo, 'años_de_servicio': matricul.años_de_servicio, 'pacientes_atendidos': matricul.pacientes_atendidos})
    
    return render(request, 'AppSalud/actualizar_matricula.html', {'form': form})

def eliminar_matricula(request, matricula_id):
    matricula = Matricula.objects.get(matricula=matricula_id)
    matricula.delete()

    matricula = matricula.objects.all()

    context = {'matricula': matricula}

    return render(request, 'AppSalud/index.html',context=context)




from django.shortcuts import render, redirect, get_object_or_404
from .models import Cobertura
from .forms import crear_Coberturas_forms  # Asegúrate de importar el formulario

def mostrar_coberturas(request):
    cobertura = Cobertura.objects.all()
    context = {'cobertura': cobertura}
    return render(request, 'AppSalud/cobertura.html', context=context)

def crear_coberturas(request):
    if request.method == 'POST':
        form = crear_Coberturas_forms(request.POST)
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            Coberturas = Cobertura(nombre_cobertura=formulario_limpio['nombre_cobertura'])
            Coberturas.save()
            return redirect('Coberturas')  # Redirige a mostrar_coberturas
    else:
        form = crear_Coberturas_forms()
    return render(request, 'AppSalud/crear_coberturas.html', {'form': form})

def buscar_nombre_cobertura(request):
    respuesta = None  
    coberturas = None  # Asegúrate de inicializar la variable coberturas

    if request.GET.get('nombre_cobertura', False):
        nombre_cobertura = request.GET['nombre_cobertura']
        coberturas = Cobertura.objects.filter(nombre_cobertura__icontains=nombre_cobertura)
        
        if coberturas.exists():
            return render(request, 'AppSalud/buscar_nombre_cobertura.html', {'coberturas': coberturas})
        else:
            respuesta = 'No se encuentra la Cobertura'
    else:
        respuesta = 'No se ha proporcionado nombre_cobertura'

    return render(request, 'AppSalud/buscar_nombre_cobertura.html', {'respuesta': respuesta})

def actualizar_coberturas(request, id_cobertura):
    cobertura = get_object_or_404(Cobertura, id_cobertura=id_cobertura)
    if request.method == 'POST':
        form = crear_Coberturas_forms(request.POST)
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            cobertura.nombre_cobertura = formulario_limpio['nombre_cobertura']
            cobertura.save()
            return redirect('Coberturas')  # Redirige a mostrar_coberturas
    else:
        form = crear_Coberturas_forms(initial={'nombre_cobertura': cobertura.nombre_cobertura})
    return render(request, 'AppSalud/actualizar_cobertura.html', {'form': form})

def eliminar_coberturas(request, id_cobertura):
    cobertura = get_object_or_404(Cobertura, id_cobertura=id_cobertura)
    cobertura.delete()
    return redirect('Coberturas')  # Redirige a mostrar_coberturas


def mostrar_especialidades(request):

    especialidad=Especialidad.objects.all()

    context={'especialidad':especialidad}

    return render(request,'AppSalud/especialidad.html',context=context)


def crear_especialidades(request):
    if request.method == 'POST':
        form= crear_Especialidades_forms(request.POST)

        if form.is_valid():

            formulario_limpio= form.cleaned_data

            especialidades= Especialidad(nombre_especialidad=formulario_limpio['nombre_especialidad'])

            especialidades.save()

            return render(request,'AppSalud/index.html')
        
    else:
        form=crear_Especialidades_forms()

        return render(request,'AppSalud/crear_especialidades.html', {'form': crear_Especialidades_forms})
    


def buscar_nombre_especialidad(request):
    if request.GET.get('nombre_especialidad', False):
        nombre_especialidad = request.GET['nombre_especialidad']
        especialidad = Especialidad.objects.filter(nombre_especialidad__icontains=nombre_especialidad)

        return render(request, 'AppSalud/buscar_nombre_especialidad.html', {'especialidades': especialidad})
    else:
        respuesta = 'No se encuentra la Especialidad'
    
    return render(request, 'AppSalud/buscar_nombre_especialidad.html', {'respuesta': respuesta})
    
    
def actualizar_especialidades(request,nombre_especialidad):
    especialidad = Especialidad.objects.get(nombre_especialidad=nombre_especialidad)
    if request.method == 'POST':
        form = crear_Especialidades_forms(request.POST)

        if form.is_valid():

            formulario_limpio = form.cleaned_data

            especialidad.nombre_especialidad = formulario_limpio['nombre_especialidad']
            especialidad.save()

            return render(request, 'AppSalud/index.html')
    
    else:
        form = crear_Especialidades_forms(initial={'nombre_especialidad': especialidad.nombre_especialidad})
    
    return render(request, 'AppSalud/actualizar_especialidad.html', {'form': crear_Especialidades_forms})

    
def eliminar_especialidades(request,nombre_especialidad):
    especialidad = Especialidad.objects.get(nombre_especialidad=nombre_especialidad)
    especialidad.delete()

    especialidad = Especialidad.objects.all()

    context = {'especialidad': especialidad}

    return render(request, 'AppSalud/index.html',context=context)





def mostrar_localidades(request):

    localidad= Localidad.objects.all()

    context={'localidad':localidad}

    return render(request,'AppSalud/localidad.html',context=context)


def crear_localidades(request):
  
    if request.method == 'POST':
        form=crear_Localidades_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            Localidades = Localidad(localidad=formulario_limpio['localidad'], provincia=formulario_limpio['provincia'])

            Localidades.save()

            return render(request, 'AppSalud/index.html')
    
    else:
        form = crear_Localidades_forms()

    return render(request, 'AppSalud/crear_localidades.html', {'form': crear_Localidades_forms})
  
    



def buscar_nombre_localidad(request):
    if 'localidad' in request.GET:
        nombre_localidad = request.GET['localidad']
        localidades = Localidad.objects.filter(localidad__icontains=nombre_localidad)
        return render(request, 'AppSalud/buscar_nombre_localidad.html', {'localidades': localidades})
    else:
        return render(request, 'AppSalud/buscar_nombre_localidad.html', {'localidades': None})
    
    
    
def actualizar_localidades(request,localidad):
    localidad = Localidad.objects.get(localidad=localidad)
    if request.method == 'POST':
        form = crear_Localidades_forms(request.POST)

        if form.is_valid():

            formulario_limpio = form.cleaned_data

            localidad.localidad = formulario_limpio['localidad']
            localidad.provincia = formulario_limpio['provincia']
            localidad.save()

            return render(request, 'AppSalud/index.html')
    
    else:
        form = crear_Localidades_forms(initial={'localidad': localidad.localidad, 'nombre_paciente': localidad.provincia})
    
    return render(request, 'AppSalud/actualizar_localidad.html', {'form': crear_Localidades_forms})



    
def eliminar_localidades(request,localidad):
    localidad = Localidad.objects.get(localidad=localidad)
    localidad.delete()

    localidad = Localidad.objects.all()

    context = {'localidad': localidad}

    return render(request, 'AppSalud/index.html',context=context)


def mostrar_sede_clinica(request):

    sede_clinica=Sede_Clinica.objects.all()

    context={'sede_clinica':sede_clinica} 

    return render(request,'AppSalud/sedeclinica.html',context=context)

def crear_sede(request):
    if request.method == 'POST':
        form=crear_Sede_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            sede = Sede_Clinica(id_localidad=formulario_limpio['id_localidad'], telefono_sede=formulario_limpio['telefono_sede'], direccion_sede=formulario_limpio['direccion_sede'], email_sede=formulario_limpio['email_sede'])

            sede.save()

            return render(request, 'AppSalud/index.html')
    
    else:
        form = crear_Sede_forms()

    return render(request, 'AppSalud/crear_sede.html', {'form': crear_Sede_forms})

def buscar_sede(request):
    
    direccion_sede = request.GET.get('direccion_sede', '')

    
    sedes = Sede_Clinica.objects.filter(direccion_sede__icontains=direccion_sede) if direccion_sede else None

    return render(request, 'AppSalud/buscar_nombre_sede.html', {'sedes': sedes})

    
    
    
def actualizar_sede(request,direccion_sede):
    sede = Sede_Clinica.objects.get(direccion_sede=direccion_sede)
    if request.method == 'POST':
        form = crear_Sede_forms(request.POST)

        if form.is_valid():

            formulario_limpio = form.cleaned_data

            sede.id_localidad = formulario_limpio['id_localidad']
            sede.telefono_sede = formulario_limpio['telefono_sede']
            sede.direccion_sede = formulario_limpio['direccion_sede']
            sede.email_sede = formulario_limpio['email_sede']
            sede.save()

            return render(request, 'AppSalud/index.html')
    
    else:
        form = crear_Sede_forms(initial={'id_localidad': sede.id_localidad, 'telefono_sede': sede.telefono_sede, 'direccion_sede': sede.direccion_sede, 'email_sede': sede.email_sede})
    
    return render(request, 'AppSalud/actualizar_sede.html', {'form': crear_Sede_forms})

    
    

def eliminar_sede(request,direccion_sede):
    sede = Sede_Clinica.objects.get(direccion_sede=direccion_sede)
    sede.delete()

    sede = Sede_Clinica.objects.all()

    context = {'sede': sede}

    return render(request, 'AppSalud/index.html',context=context)






def mostrar_medicos(request):
    medico=Medicos.objects.all()
    
    context={'medico':medico}
    
    return render(request,'AppSalud/medicos.html', context=context)



def mostrar_Pacientes(request):
    paciente = Pacientes.objects.all()

    context = {'paciente': paciente}

    return render(request, 'AppSalud/pacientes.html', context=context)



def crear_pacientes(request):
    if request.method == 'POST':
        form = crear_Pacientes_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            
            pacientes = Pacientes(
                id_dni=formulario_limpio['id_dni'], 
                nombre_paciente=formulario_limpio['nombre_paciente'], 
                apellido_paciente=formulario_limpio['apellido_paciente'], 
                fecha_nacimiento=formulario_limpio['fecha_nacimiento'], 
                sexo_paciente=formulario_limpio['sexo_paciente'], 
                id_cobertura=formulario_limpio['id_cobertura'], 
                id_localidad=formulario_limpio['id_localidad']
            )

            pacientes.save()

            
            return render(request, 'AppSalud/index.html')
    
    else:
        form = crear_Pacientes_forms()

    # Asegurarse de pasar la instancia `form`
    return render(request, 'AppSalud/crear_paciente.html', {'form': form})




def buscar_nombre_Pacientes(request):
    if request.GET.get('nombre_paciente', False):
        nombre_paciente = request.GET['nombre_paciente']
        paciente = Pacientes.objects.filter(nombre_paciente__icontains=nombre_paciente)

        return render(request, 'AppSalud/buscar_nombre_paciente.html', {'pacientes': paciente})
    else:
        respuesta = 'No se encuentra Paciente'
    
    return render(request, 'AppSalud/buscar_nombre_paciente.html', {'respuesta': respuesta})




def eliminar_paciente(request, paciente_id):
    paciente = Pacientes.objects.get(id_dni=paciente_id)
    paciente.delete()

    paciente = paciente.objects.all()

    context = {'paciente': paciente}

    return render(request, 'AppSalud/index.html',context=context)

def actualizar_paciente(request, paciente_id):
    paciente = Pacientes.objects.get(id_dni=paciente_id)
    if request.method == 'POST':
        form = crear_Pacientes_forms(request.POST)

        if form.is_valid():

            formulario_limpio = form.cleaned_data

            paciente.id_dni = formulario_limpio['id_dni']
            paciente.nombre_paciente = formulario_limpio['nombre_paciente']
            paciente.apellido_paciente = formulario_limpio['apellido_paciente']
            paciente.fecha_nacimiento = formulario_limpio['fecha_nacimiento']
            paciente.sexo_paciente = formulario_limpio['sexo_paciente']
            paciente.id_cobertura = formulario_limpio['id_cobertura']
            paciente.id_localidad = formulario_limpio['id_localidad']
            paciente.save()

            return render(request, 'AppSalud/index.html')
    
    else:
        form = crear_Pacientes_forms(initial={'id_dni': paciente.id_dni, 'nombre_paciente': paciente.nombre_paciente, 'apellido_paciente': paciente.apellido_paciente, 'fecha_nacimiento': paciente.fecha_nacimiento, 'sexo_paciente': paciente.sexo_paciente, 'id_cobertura': paciente.id_cobertura, 'id_localidad': paciente.id_localidad})
    
    return render(request, 'AppSalud/actualizar_paciente.html', {'form': crear_Pacientes_forms})


def registro_usuario(request):
    if request.method =="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso!Bienvenido/a')
            return render(request,'AppSalud/index.html')
    else:
        form=UserRegisterForm()
        
    return render(request,'AppSalud/registro.html', {'form':form})

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario= form.cleaned_data.get('username')
            contra= form.cleaned_data.get('password')
            
            user= authenticate(username=usuario, password=contra)
            
            
            if user is not None:
                login(request,user)
                
                return render(request,'AppSalud/index.html',{"mensaje":f"Bienvenido {usuario}"})
            
            else:
                return render(request,"AppSalud/index.html",{"mensaje":"Error,datos incorrectos"})
            
        else:
            return render(request,"AppSalud/index.html",{"mensaje":"Error,formulario erroneo"})
        
    form = AuthenticationForm()
    
    return render(request,"AppSalud/login.html",{'form':form})


def logout_request(request):
    logout(request)
    return render(request,"AppSalud/index.html",{"mensaje":"Has cerrado sesion exitosamente"})
