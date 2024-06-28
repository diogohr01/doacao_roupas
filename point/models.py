from django.db import models

# Create your models here.
class PontoColeta(models.Model):
	endereco = models.CharField(max_length=255)
	cidade = models.CharField(max_length=100)
	estado = models.CharField(max_length=100)
	cep = models.CharField(max_length=20)
	criado_em = models.DateTimeField(auto_now_add=True)
	atualizado_em = models.DateTimeField(auto_now=True)

    
    