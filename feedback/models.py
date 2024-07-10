from django.db import models
from accounts.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Feedback(models.Model):
    doador = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    stars = models.FloatField(
        validators=[
            MinValueValidator(0, 'Avaliação não pode ser inferior a 0 estrelas.'),
            MaxValueValidator(5, 'Avaliação não pode ser superior a 5 estrelas.'),
        ]
    )
    