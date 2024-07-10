from django.db import models

class CatalogoRoupas(models.Model):
    TIPO_CHOICES = (
        ('camiseta', 'Camiseta'),
        ('calca', 'Calça'),
        ('bermuda', 'Bermuda'),
        ('tenis', 'Tenis'),
        ('casaco', 'Casaco'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='camiseta')
    tamanho = models.CharField(max_length=10, blank=True, null=True)
    CONDICAO_CHOICES = (
        ('novo', 'Novo'),
        ('bom', 'Bom'),
        ('razoavel', 'Razoável'),
    )
    condicao = models.CharField(max_length=10, choices=CONDICAO_CHOICES)
    quantidade = models.IntegerField()  # quantidade de roupas disponíveis
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
