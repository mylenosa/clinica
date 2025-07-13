# Arquivo: core/admin.py

from django.contrib import admin
from .models import Ambulatorio, Convenio, Consulta, Medico, Paciente

@admin.register(Ambulatorio)
class AmbulatorioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'andar', 'numleitos')
    search_fields = ('nome',)
    list_filter = ('andar',)

@admin.register(Convenio)
class ConvenioAdmin(admin.ModelAdmin):
    list_display = ('codconv', 'nome')
    search_fields = ('nome',)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('data', 'horario', 'medico', 'paciente', 'convenio')
    search_fields = ('medico__nome', 'paciente__nome', 'convenio__nome')
    list_filter = ('data', 'convenio__nome')
    autocomplete_fields = ('medico', 'paciente', 'convenio')
    date_hierarchy = 'data'

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'especialidade', 'ambulatorio', 'salario_formatado')
    search_fields = ('nome', 'crm', 'especialidade')
    list_filter = ('especialidade', 'ambulatorio__nome')
    autocomplete_fields = ('ambulatorio',)

    @admin.display(description='Salário')
    def salario_formatado(self, obj):
        if obj.salario:
            return f"R$ {obj.salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return "Não informado"

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'idade', 'ambulatorio')
    search_fields = ('nome', 'cidade')
    list_filter = ('cidade', 'ambulatorio__nome')
    autocomplete_fields = ('ambulatorio',)
