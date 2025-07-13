from django.urls import path
from . import views

urlpatterns = [
    path('relatorios/consultas/', views.relatorio_consultas, name='relatorio_consultas'),
    path('relatorios/pacientes-por-ambulatorio/', views.relatorio_pacientes_por_ambulatorio, name='relatorio_pacientes_ambulatorio'),
    path('relatorios/medicos-por-convenio/', views.relatorio_medicos_por_convenio, name='relatorio_medicos_convenio'),
    path('graficos/pacientes-por-ambulatorio/', views.grafico_pacientes_por_ambulatorio, name='grafico_pacientes_ambulatorio'),
    path('graficos/medicos-por-convenio/', views.grafico_medicos_por_convenio, name='grafico_medicos_convenio'),
    path('graficos/consultas-por-dia/', views.grafico_consultas_por_dia, name='grafico_consultas_dia'),
    path('', views.dashboard, name='dashboard'),
    path('dashboard/pdf/', views.DashboardPDFView.as_view(), name='dashboard_pdf'),
    path('pdf/consultas/', views.RelatorioConsultasPDF.as_view(), name='pdf_consultas'),
    path('pdf/pacientes-ambulatorio/', views.RelatorioPacientesAmbulatorioPDF.as_view(), name='pdf_pacientes_ambulatorio'),
    path('pdf/medicos-convenio/', views.RelatorioMedicosConvenioPDF.as_view(), name='pdf_medicos_convenio'),
]