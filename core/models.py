from django.db import models


class Ambulatorio(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)
    numleitos = models.IntegerField(blank=True, null=True)
    andar = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ambulatorio'

    def __str__(self):
        return self.nome


class Convenio(models.Model):
    codconv = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'convenio'

    def __str__(self):
        return self.nome


class Medico(models.Model):
    crm = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    especialidade = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=250, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    salario = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ambulatorio = models.ForeignKey(Ambulatorio, on_delete=models.DO_NOTHING, db_column='idamb', blank=True, null=True)
    convenios = models.ManyToManyField(Convenio, through='Atende')

    class Meta:
        db_table = 'medico'

    def __str__(self):
        return self.nome


class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=250, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    ambulatorio = models.ForeignKey(Ambulatorio, on_delete=models.DO_NOTHING, db_column='idamb', blank=True, null=True)
    convenios = models.ManyToManyField(Convenio, through='Possui')

    class Meta:
        db_table = 'paciente'

    def __str__(self):
        return self.nome


class Consulta(models.Model):
    data = models.DateField(blank=True, null=True)
    horario = models.TimeField(blank=True, null=True)
    medico = models.ForeignKey(Medico, on_delete=models.DO_NOTHING, db_column='medico', blank=True, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING, db_column='paciente', blank=True, null=True)
    convenio = models.ForeignKey(Convenio, on_delete=models.DO_NOTHING, db_column='convenio', blank=True, null=True)
    porcent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'consulta'

    def __str__(self):
        return f'{self.data} - {self.medico} - {self.paciente}'


class Atende(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.DO_NOTHING, db_column='medico', primary_key=True)
    convenio = models.ForeignKey(Convenio, on_delete=models.DO_NOTHING, db_column='convenio')

    class Meta:
        db_table = 'atende'
        unique_together = (('medico', 'convenio'),)

    def __str__(self):
        return f'{self.medico} atende {self.convenio}'


class Possui(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING, db_column='paciente', primary_key=True)
    convenio = models.ForeignKey(Convenio, on_delete=models.DO_NOTHING, db_column='convenio')
    tipo = models.CharField(max_length=1, blank=True, null=True)
    vencimento = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'possui'
        unique_together = (('paciente', 'convenio'),)

    def __str__(self):
        return f'{self.paciente} possui {self.convenio}'
