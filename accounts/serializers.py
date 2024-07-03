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
        name = data.get('name')
        
        if senha and confirm_senha and senha != confirm_senha:
            raise serializers.ValidationError("As senhas não coincidem.")
        elif len(senha) < 8:
            raise serializers.ValidationError("Senha precisa ter mais de 8 caracteres")
        elif User.objects.filter(name=name).exists():
            raise serializers.ValidationError({'non_field_errors': 'Já existe usuário com esse nome.'})


        #user = User.objects.get(name=data.get('name'))
        #if not user.check_senha(senha):
        #    raise serializers.ValidationError({'detail': 'Senha inválida'})
        #if user.name == name:
        #    raise serializers.ValidationError({'name': 'Usuário não encontrado'})
        return data
    
    def get_user_by_name(self, name):
        try:
            return User.objects.get(name=name)
        except User.DoesNotExist:
            raise serializers.ValidationError({'name': 'Usuário não encontrado.'})
    
    def get_user_by_senha(self, senha):
        try:
            return User.objects.get(senha=senha)
        except User.DoesNotExist:
            raise serializers.ValidationError({'senha': 'Senha inválida.'})
    

    def create(self, validated_data):

        validated_data.pop('confirm_senha')
        user = User.objects.create(**validated_data)
        senha = validated_data.pop('senha')
        salt = bcrypt.gensalt()
        hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), salt)
        user.senha = hashed_senha.decode('utf-8')
        user.save()

        doador = validated_data.get('is_doador')
        beneficiario = validated_data.get('is_beneficiario')

        if not doador and not beneficiario:
            raise serializers.ValidationError({'non_field_errors': 'Você deve escolher se você é doador ou beneficiário'})
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

    
    
    
class UserLoginSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'senha']

    def validate(self, data):
        user = User.objects.get(name=data.get('name'))
        if not user.check_senha(data.get('senha')):
            raise serializers.ValidationError({'detail': 'Senha inválida'})
        return data    
    
    
    
        
    

    
    

   

    


    
        
