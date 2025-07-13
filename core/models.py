# Arquivo: core/models.py

from django.db import models

class Ambulatorio(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    numleitos = models.IntegerField(blank=True, null=True)
    andar = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ambulatorio'
        verbose_name = "Ambulatório"
        verbose_name_plural = "Ambulatórios"

    def __str__(self):
        return f"{self.nome} ({self.andar}º andar)"

class Convenio(models.Model):
    codconv = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'convenio'
        verbose_name = "Convênio"
        verbose_name_plural = "Convênios"

    def __str__(self):
        return self.nome

class Medico(models.Model):
    crm = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    especialidade = models.CharField(max_length=100, blank=True, null=True)
    salario = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ambulatorio = models.ForeignKey(
        Ambulatorio, models.DO_NOTHING, db_column='idamb', blank=True, null=True, related_name='medicos'
    )

    class Meta:
        managed = False
        db_table = 'medico'
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"

    def __str__(self):
        return f"{self.nome} (CRM: {self.crm})"

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    ambulatorio = models.ForeignKey(
        Ambulatorio, models.DO_NOTHING, db_column='idamb', blank=True, null=True, related_name='pacientes'
    )

    class Meta:
        managed = False
        db_table = 'paciente'
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField(blank=True, null=True)
    horario = models.TimeField(blank=True, null=True)
    medico = models.ForeignKey(
        'Medico', models.DO_NOTHING, db_column='medico', related_name='consultas'
    )
    paciente = models.ForeignKey(
        'Paciente', models.DO_NOTHING, db_column='paciente', related_name='consultas'
    )
    convenio = models.ForeignKey(
        'Convenio', models.DO_NOTHING, db_column='convenio', related_name='consultas'
    )

    class Meta:
        managed = False
        db_table = 'consulta'
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

    def __str__(self):
        paciente_nome = self.paciente.nome if self.paciente else "N/A"
        medico_nome = self.medico.nome if self.medico else "N/A"
        data_str = self.data.strftime('%d/%m/%Y') if self.data else "N/A"
        return f"Consulta de {paciente_nome} com Dr(a). {medico_nome} em {data_str}"
