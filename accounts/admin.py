from django.contrib import admin
from accounts.models import User
import bcrypt

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_doador', 'is_beneficiario', 'email', 'senha', 'birthday']
    
    
    
    
    
    