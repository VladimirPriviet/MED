# app/models.py
from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    email = models.EmailField(max_length=254, blank=True, null=True, verbose_name="Email")
    telefone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefone")
    endereco = models.CharField(max_length=255, blank=True, null=True, verbose_name="Endereço")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

class Sintoma(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do Sintoma")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição do Sintoma")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Sintoma"
        verbose_name_plural = "Sintomas"

class Doenca(models.Model): 
    nome = models.CharField(max_length=200, unique=True, verbose_name="Nome da Doença")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição da Doença")
    sintomas_comuns = models.ManyToManyField(Sintoma, blank=True, verbose_name="Sintomas Comuns")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Doença"
        verbose_name_plural = "Doenças"

class Diagnostico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    doenca = models.ForeignKey(Doenca, on_delete=models.CASCADE, verbose_name="Doença Diagnosticada") 
    data_diagnostico = models.DateField(auto_now_add=True, verbose_name="Data do Diagnóstico")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações do Diagnóstico")
    arquivo_diagnostico = models.FileField(upload_to='diagnosticos/', blank=True, null=True, verbose_name="Anexar Arquivo")

    def __str__(self):
        return f"Diagnóstico de {self.doenca.nome} para {self.paciente.nome} em {self.data_diagnostico}"

    class Meta:
        verbose_name = "Diagnóstico"
        verbose_name_plural = "Diagnósticos"
        ordering = ['-data_diagnostico']
        
class Consulta(models.Model):
    data = models.DateField(verbose_name="Data da Consulta")
    horario = models.TimeField(verbose_name="Horário")
    medico = models.CharField(max_length=100, verbose_name="Médico Responsável")
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Diagnóstico")

    def __str__(self):
        return f"{self.paciente.nome} - {self.data} às {self.horario}"

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
        ordering = ['-data', '-horario']



