from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # URLs dos Relatórios
    path('relatorios/pacientes-por-cidade/', views.relatorio_pacientes_por_cidade, name='relatorio_pacientes_cidade'),
    path('relatorios/consultas-por-medico/', views.relatorio_consultas_por_medico, name='relatorio_consultas_medico'),
    path('relatorios/convenios-utilizados/', views.relatorio_convenios_utilizados, name='relatorio_convenios'),
]