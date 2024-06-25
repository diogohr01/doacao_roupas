from rest_framework import serializers
from accounts.models import User

class CustomTokenObtainPairSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    senha = serializers.CharField(max_length=128, write_only=True)

    def validate(self, attrs):
        name = attrs.get('name')
        senha = attrs.get('senha')

        users = User.objects.filter(name=name)
        if users.count() > 1:
            raise serializers.ValidationError({'name': 'Multiple users with the same name'})
        elif users.count() == 0:
            raise serializers.ValidationError({'name': 'User not found'})

        user = users.first()
        if not user.check_password(senha):
            raise serializers.ValidationError({'senha': 'Senha incorreta'})

        return {'user': user}