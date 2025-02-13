from django.db import models
from accounts.models import User
from point.models import PontoColeta 
from catalog.models import CatalogoRoupas
# Create your models here.
class AgendamentoDoacao(models.Model):
    doador = models.ForeignKey(User, on_delete=models.CASCADE)
    ponto_coleta = models.ForeignKey(PontoColeta, on_delete=models.CASCADE)
    catalog = models.ForeignKey(CatalogoRoupas, on_delete=models.CASCADE, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    data_hora_agendada = models.CharField(max_length=20, blank=True)
    STATUS_CHOICES = (
        ('agendado', 'Agendado'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='agendado')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    
    
