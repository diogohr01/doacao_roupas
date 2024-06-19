from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        
    def validate(self, data):
        senha = data.get('senha')
        confirm_senha = data.get('confirm_senha')
        
        if senha != confirm_senha:
            raise serializers.ValidationError("As senhas não coincidem.")
        
        return data
        
    
        
