

# Register your models here.
from django.contrib import admin
from donation.models import AgendamentoDoacao
import bcrypt

# Register your models here.
@admin.register(AgendamentoDoacao)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'doador', 'ponto_coleta', 'data_hora_agendada', 'status', 'criado_em', 'atualizado_em')
    
   