
from django.contrib import admin
from catalog.models import CatalogoRoupas
import bcrypt

# Register your models here.
@admin.register(CatalogoRoupas)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'tamanho', 'condicao', 'quantidade', 'criado_em', 'atualizado_em')
    

