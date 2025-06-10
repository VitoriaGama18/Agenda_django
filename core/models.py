from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=10)
    telefone = models.IntegerField()
    email = models.EmailField(blank=True)
    descricao = models.TextField(max_length=255)

