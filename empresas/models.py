from datetime import datetime

from django.db import models

# Create your models here.

class Empresas(models.Model):
    nome = models.CharField(max_length= 30)
    def __str__(self):
        return self.nome

class Acao(models.Model):
    sigla = models.CharField(max_length=10)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE, related_name='empresa')
    data = models.DateTimeField(default=datetime.now())

    class meta:
        ordering = ['-data']

class Cotacao(models.Model):
    data = models.DateField(default=datetime.now())
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE, related_name='acao')
    valor = models.FloatField(null=False)

    class meta:
        ordering =['-data']