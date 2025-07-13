from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db.models import Count
from .models import Consulta, Ambulatorio, Convenio, Consulta
from django.http import HttpResponse
from django.views import View
from .utils import GeraPDFMixin
import plotly.graph_objs as go

def relatorio_consultas(request):
    consultas = Consulta.objects.select_related('medico', 'paciente', 'convenio').order_by('-data')
    return render(request, 'relatorios/relatorio_consultas.html', {'consultas': consultas})

def relatorio_pacientes_por_ambulatorio(request):
    dados = (
        Ambulatorio.objects
        .annotate(total_pacientes=Count('paciente'))
        .order_by('-total_pacientes')
    )
    return render(request, 'relatorios/relatorio_pacientes_ambulatorio.html', {'dados': dados})


def relatorio_medicos_por_convenio(request):
    dados = (
        Convenio.objects
        .annotate(total_medicos=Count('medico'))
        .order_by('-total_medicos')
    )
    return render(request, 'relatorios/relatorio_medicos_convenio.html', {'dados': dados})


def grafico_pacientes_por_ambulatorio(request):
    dados = (
        Ambulatorio.objects
        .annotate(total_pacientes=Count('paciente'))
        .order_by('nome')
    )

    labels = [amb.nome for amb in dados]
    valores = [amb.total_pacientes for amb in dados]

    return render(request, 'graficos/grafico_pacientes_ambulatorio.html', {
        'labels': labels,
        'valores': valores
    })


def grafico_medicos_por_convenio(request):
    dados = (
        Convenio.objects
        .annotate(total_medicos=Count('medico'))
        .filter(total_medicos__gt=0)
        .order_by('nome')
    )

    labels = [conv.nome for conv in dados]
    valores = [conv.total_medicos for conv in dados]

    return render(request, 'graficos/grafico_medicos_convenio.html', {
        'labels': labels,
        'valores': valores
    })


def grafico_consultas_por_dia(request):
    dados = (
        Consulta.objects
        .values('data')
        .annotate(total=Count('id'))
        .order_by('data')
    )

    datas = [str(item['data']) for item in dados]
    totais = [item['total'] for item in dados]

    trace = go.Bar(x=datas, y=totais, marker=dict(color='rgba(255,99,132,0.6)'))
    layout = go.Layout(title='Consultas por Dia', xaxis=dict(title='Data'), yaxis=dict(title='Quantidade'))
    fig = go.Figure(data=[trace], layout=layout)
    grafico_html = fig.to_html(full_html=False)

    return render(request, 'graficos/grafico_consultas_plotly.html', {'grafico': grafico_html})




def dashboard(request):
    # Gráfico 1: Pacientes por ambulatório
    ambulatorios = (
        Ambulatorio.objects
        .annotate(total_pacientes=Count('paciente'))
        .order_by('nome')
    )
    labels_amb = [amb.nome for amb in ambulatorios]
    valores_amb = [amb.total_pacientes for amb in ambulatorios]

    # Gráfico 2: Médicos por convênio
    convenios = (
        Convenio.objects
        .annotate(total_medicos=Count('medico'))
        .filter(total_medicos__gt=0)
        .order_by('nome')
    )
    labels_conv = [c.nome for c in convenios]
    valores_conv = [c.total_medicos for c in convenios]

    # Gráfico 3: Consultas por dia (Plotly)
    consultas = (
        Consulta.objects
        .values('data')
        .annotate(total=Count('id'))
        .order_by('data')
    )
    datas = [str(item['data']) for item in consultas]
    totais = [item['total'] for item in consultas]
    plotly_trace = go.Bar(x=datas, y=totais, marker=dict(color='rgba(255,99,132,0.6)'))
    plotly_layout = go.Layout(title='Consultas por Dia', xaxis=dict(title='Data'), yaxis=dict(title='Quantidade'))
    plotly_fig = go.Figure(data=[plotly_trace], layout=plotly_layout)
    plotly_html = plotly_fig.to_html(full_html=False)

    return render(request, 'dashboard.html', {
        'labels_amb': labels_amb,
        'valores_amb': valores_amb,
        'labels_conv': labels_conv,
        'valores_conv': valores_conv,
        'plotly_html': plotly_html,
    })




class RelatorioConsultasPDF(View, GeraPDFMixin):
    def get(self, request):
        consultas = Consulta.objects.select_related('medico', 'paciente', 'convenio').order_by('-data')
        contexto = {'consultas': consultas}
        return self.criar_pdf('relatorios/relatorio_consultas.html', contexto)


class RelatorioPacientesAmbulatorioPDF(View, GeraPDFMixin):
    def get(self, request):
        dados = (
            Ambulatorio.objects
            .annotate(total_pacientes=Count('paciente'))
            .order_by('nome')
        )
        contexto = {'dados': dados}
        return self.criar_pdf('relatorios/relatorio_pacientes_ambulatorio.html', contexto)


class RelatorioMedicosConvenioPDF(View, GeraPDFMixin):
    def get(self, request):
        dados = (
            Convenio.objects
            .annotate(total_medicos=Count('medico'))
            .filter(total_medicos__gt=0)
            .order_by('nome')
        )
        contexto = {'dados': dados}
        return self.criar_pdf('relatorios/relatorio_medicos_convenio.html', contexto)



class DashboardPDFView(View, GeraPDFMixin):
    def get(self, request):
        ambulatorios = (
            Ambulatorio.objects
            .annotate(total_pacientes=Count('paciente'))
            .order_by('nome')
        )
        convenios = (
            Convenio.objects
            .annotate(total_medicos=Count('medico'))
            .filter(total_medicos__gt=0)
            .order_by('nome')
        )
        consultas = (
            Consulta.objects
            .values('data')
            .annotate(total=Count('id'))
            .order_by('data')
        )
        contexto = {
            'ambulatorios': ambulatorios,
            'convenios': convenios,
            'consultas': consultas,
        }
        return self.criar_pdf('dashboard_pdf.html', contexto)