from django.db import models

class User(models.Model):
    is_doador = models.BooleanField(default=False)
    is_beneficiario = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True, blank=True)  # Use EmailField para validação embutida
    senha = models.CharField(max_length=16)
    birthday = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name
