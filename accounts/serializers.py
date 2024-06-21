from rest_framework import serializers
from accounts.models import User
import bcrypt

class UserSerializer(serializers.ModelSerializer):
    confirm_senha = serializers.CharField(write_only=True)  # Define confirm_senha as write-only
    senha = serializers.CharField(write_only=True)  # Define senha as write-only
    
    class Meta:
        model = User
        fields = ['id', 'name', 'is_doador', 'is_beneficiario', 'email', 'senha', 'confirm_senha', 'birthday']
        
    
    def validate(self, data):
        senha = data.get('senha')
        confirm_senha = data.get('confirm_senha')
        
        if senha and confirm_senha and senha != confirm_senha:
            raise serializers.ValidationError("As senhas não coincidem.")
        elif len(senha) < 8:
            raise serializers.ValidationError("Senha precisa ter mais de 8 caracteres")
        
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_senha') 
        senha = validated_data.pop('senha').encode('utf-8')
        salt = bcrypt.gensalt()  
        hash_senha = bcrypt.hashpw(senha, salt).decode('utf-8')
        validated_data['senha'] = hash_senha
        user = User.objects.create(**validated_data)
        
        doador = validated_data.get('is_doador')
        beneficiario = validated_data.get('is_beneficiario') 
        
        if not doador and not beneficiario:
            raise serializers.ValidationError("Você deve escolher pelo menos uma opção: doador ou beneficiário.")
        return user

    def update(self, instance, validated_data):
        if 'senha' in validated_data:
            senha = validated_data.pop('senha').encode('utf-8')
            salt = bcrypt.gensalt()
            hash_senha = bcrypt.hashpw(senha, salt).decode('utf-8')
            instance.senha = hash_senha

        if 'confirm_senha' in validated_data:
            validated_data.pop('confirm_senha')
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance

    
    
    
    
    
    
    
        
    

    
    

   

    


    
        
