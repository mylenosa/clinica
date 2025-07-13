from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Ambulatorio, Medico, Paciente, Convenio, Consulta, Atende, Possui


@admin.register(Ambulatorio)
class AmbulatorioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numleitos', 'andar')
    search_fields = ('nome',)


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('crm', 'nome', 'especialidade', 'idade', 'salario', 'ambulatorio')
    list_filter = ('especialidade', 'ambulatorio')
    search_fields = ('nome', 'crm')


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'cidade', 'ambulatorio')
    search_fields = ('nome', 'cidade')
    list_filter = ('ambulatorio',)


@admin.register(Convenio)
class ConvenioAdmin(admin.ModelAdmin):
    list_display = ('codconv', 'nome')
    search_fields = ('nome',)


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('data', 'horario', 'medico', 'paciente', 'convenio', 'porcent')
    list_filter = ('data', 'medico', 'convenio')


@admin.register(Atende)
class AtendeAdmin(admin.ModelAdmin):
    list_display = ('medico', 'convenio')


@admin.register(Possui)
class PossuiAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'convenio', 'tipo', 'vencimento')
    list_filter = ('tipo',)