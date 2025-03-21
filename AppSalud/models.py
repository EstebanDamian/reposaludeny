from django.db import models

# Create your models here.

# 1 
class Metodo_de_Pago(models.Model):
    forma_de_pago = models.CharField(max_length=30)

    def __str__(self):
        return f"Forma de Pago: {self.forma_de_pago}"

#2
class Sin_Cobertura(models.Model):
    id_metodo_de_pago = models.ForeignKey(Metodo_de_Pago, on_delete=models.CASCADE)
    monto = models.FloatField()

    def __str__(self):
        return f"ID Metodo de Pago: {self.id_metodo_de_pago}, Monto: {self.monto}"
    
#3
class Prepaga(models.Model):
    nombre_prepaga = models.CharField(max_length=30)
    plan = models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre Prepaga: {self.nombre_prepaga}, Plan: {self.plan}"
    
#4
class Obra_Social(models.Model):
    nombre_obra_social = models.CharField(max_length=30)
    plan = models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre Obra Social: {self.nombre_obra_social}, Plan: {self.plan}"

#5
class Cobertura(models.Model):
    nombre_cobertura = models.CharField(max_length=100)
  

    def __str__(self):
        return f"Nombre Cobertura: {self.nombre_cobertura}"

#6
class Localidad(models.Model):
    localidad = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)

    def __str__(self):
        return f"Localidad: {self.localidad}, Provincia: {self.provincia}"

#7
class Pacientes(models.Model):
    id_dni = models.IntegerField(primary_key=True)
    nombre_paciente = models.CharField(max_length=30)
    apellido_paciente = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    sexo_paciente = models.CharField(max_length=30)
    id_cobertura = models.ForeignKey(Cobertura, on_delete=models.CASCADE)
    id_localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"DNI(paciente): {self.id_dni}, Nombre(paciente): {self.nombre_paciente}, Apellido(paciente): {self.apellido_paciente}, Fecha de Nacimiento: {self.fecha_nacimiento}, Sexo: {self.sexo_paciente}, ID Cobertura: {self.id_cobertura}, ID Localidad: {self.id_localidad}"
    

#8
class Sede_Clinica(models.Model):
    id_localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    telefono_sede = models.IntegerField(max_length=30)
    direccion_sede = models.CharField(max_length=30)
    email_sede = models.EmailField()

    def __str__(self):
        return f"ID Localidad: {self.id_localidad}, Telefono: {self.telefono_sede}, Direccion: {self.direccion_sede}, E-Mail: {self.email_sede}"
    
#9
class Consultorio(models.Model):
    id_numero = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"Numero: {self.id_numero}"

#10
class Numero_de_Turno(models.Model):
    id_turno = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    id_numero_de_consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE)
    id_sede = models.ForeignKey(Sede_Clinica, on_delete=models.CASCADE)
    id_dni_paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)

    def __str__(self):
        return f"Turno: {self.id_turno}, Fecha: {self.fecha}, Hora: {self.hora}, N° Consultorio: {self.id_numero_de_consultorio}, ID Sede: {self.id_sede}, DNI: {self.id_dni_paciente}"

#11
class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=30)

    def __str__(self):
        return f"Especialidad: {self.nombre_especialidad}"
    
#12
class Matricula(models.Model):
    matricula = models.IntegerField(primary_key=True)
    numero_legajo = models.IntegerField(max_length=30)
    años_de_servicio = models.IntegerField(max_length=10)
    pacientes_atendidos = models.IntegerField(max_length=10)

    def __str__(self):
        return f"Matricula: {self.matricula}, N° Legajo: {self.numero_legajo}, Años de Servicio: {self.años_de_servicio}, Pacientes Atendidos: {self.pacientes_atendidos}"
    
#13
class Medicos(models.Model):
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    nombre_medico = models.CharField(max_length=30)
    apellido_medico = models.CharField(max_length=30)
    dni_medico = models.IntegerField(max_length=30)
    id_matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    id_numero_de_consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE)
    id_sede = models.ForeignKey(Sede_Clinica, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID Especialidad: {self.id_especialidad}, Nombre(medico): {self.nombre_medico}, Apellido(medico): {self.apellido_medico}, DNI(medico): {self.dni_medico}, ID Matricula: {self.id_matricula}, N° Consultorio: {self.id_numero_de_consultorio}, ID Sede: {self.id_sede}"

#14
class Sistema_de_Turnos(models.Model):
    id_numero_de_turno = models.ForeignKey(Numero_de_Turno, on_delete=models.CASCADE)
    id_dni_paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    id_medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)

    def __str__(self):
        return f"N° Turno: {self.id_numero_de_turno}, DNI(paciente): {self.id_dni_paciente}, Especialidad: {self.id_especialidad}, ID Medico: {self.id_medico}"
