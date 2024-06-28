# Register your models here.
from django.contrib import admin
from point.models import PontoColeta
import bcrypt

# Register your models here.
@admin.register(PontoColeta)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'endereco', 'cidade', 'estado', 'cep', 'criado_em', 'atualizado_em')

