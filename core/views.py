# Arquivo: core/views.py

from django.shortcuts import render
from django.db.models import Count
from .models import Paciente, Medico, Consulta, Convenio
import plotly.express as px
import json

# --- PÁGINA PRINCIPAL / DASHBOARD ---
def dashboard(request):
    # Gráfico 1: Consultas por dia (usando Plotly)
    consultas_por_dia = Consulta.objects.values('data').annotate(total=Count('id')).order_by('data')
    fig_consultas = px.line(
        x=[item['data'] for item in consultas_por_dia],
        y=[item['total'] for item in consultas_por_dia],
        labels={'x': 'Data', 'y': 'Número de Consultas'},
        title='Volume de Consultas por Dia',
        markers=True
    )
    fig_consultas.update_layout(title_x=0.5)
    grafico_consultas_html = fig_consultas.to_html(full_html=False)

    # Gráfico 2: Pacientes por ambulatório (para Chart.js)
    pacientes_por_ambulatorio = Paciente.objects.values('ambulatorio__nome').annotate(total=Count('id')).order_by('-total')
    labels_pac_amb = [item['ambulatorio__nome'] for item in pacientes_por_ambulatorio]
    data_pac_amb = [item['total'] for item in pacientes_por_ambulatorio]

    # Gráfico 3: Médicos por especialidade (para Chart.js - tipo "Doughnut")
    medicos_por_especialidade = Medico.objects.values('especialidade').annotate(total=Count('crm')).order_by('-total')
    labels_med_esp = [item['especialidade'] for item in medicos_por_especialidade]
    data_med_esp = [item['total'] for item in medicos_por_especialidade]

    context = {
        'grafico_consultas_html': grafico_consultas_html,
        'labels_pac_amb': json.dumps(labels_pac_amb),
        'data_pac_amb': json.dumps(data_pac_amb),
        'labels_med_esp': json.dumps(labels_med_esp),
        'data_med_esp': json.dumps(data_med_esp),
    }
    return render(request, 'dashboard.html', context)


# --- RELATÓRIOS ---
def relatorio_pacientes_por_cidade(request):
    dados = Paciente.objects.values('cidade').annotate(total=Count('id')).order_by('-total')
    context = {
        'titulo': 'Relatório de Pacientes por Cidade',
        'dados': dados,
        'colunas': ['Cidade', 'Total de Pacientes'],
        'tipo': 'paciente_cidade'
    }
    return render(request, 'relatorio_geral.html', context)


def relatorio_consultas_por_medico(request):
    dados = Medico.objects.annotate(total_consultas=Count('consultas')).order_by('-total_consultas')
    context = {
        'titulo': 'Relatório de Consultas por Médico',
        'dados': dados,
        'colunas': ['Médico', 'Especialidade', 'Total de Consultas'],
        'tipo': 'medico'
    }
    return render(request, 'relatorio_geral.html', context)


def relatorio_convenios_utilizados(request):
    # O seu banco de dados 'convenio' não tem a coluna 'plano', então ela foi removida da busca.
    dados = Consulta.objects.values('convenio__nome').annotate(total=Count('id')).order_by('-total')
    context = {
        'titulo': 'Relatório de Utilização de Convênios',
        'dados': dados,
        'colunas': ['Convênio', 'Nº de Vezes Utilizado'],
        'tipo': 'convenio'
    }
    return render(request, 'relatorio_geral.html', context)
