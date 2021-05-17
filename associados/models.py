from django.db import models
from datetime import datetime

class Sindicato(models.Model):
    razao_social = models.CharField(max_length=200)
    fantasia     = models.CharField(max_length=200)
    cnpj         = models.CharField(max_length=15)
    dt_fundacao  = models.DateField

    class Meta:
        db_table = "sindicato"

class Associado(models.Model):
    nome = models.CharField(max_length=200)
    cpf  = models.CharField(max_length=15)
    dt_nascimento = models.DateField
    dt_cadastro = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = "associado"
