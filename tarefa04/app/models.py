from django.db import models

class Atividade(models.Model):
    nome = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    prazo = models.CharField(max_length=50)

