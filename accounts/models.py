from django.db import models
from django.contrib.auth.hashers import check_password, make_password
import bcrypt

class User(models.Model):
    is_doador = models.BooleanField(default=False)
    is_beneficiario = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True, blank=True)  # Use EmailField para validação embutida
    senha = models.CharField(max_length=128)  # Increase max_length to accommodate hashed passwords
    birthday = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def set_senha(self, raw_senha):
        salt = bcrypt.gensalt()
        hashed_senha = bcrypt.hashpw(raw_senha.encode('utf-8'), salt)
        self.senha = hashed_senha.decode('utf-8')
        self.save()


    def check_senha(self, raw_senha):
        if bcrypt.checkpw(raw_senha.encode('utf-8'), self.senha.encode('utf-8')):
            return True
        return False
    