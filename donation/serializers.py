from rest_framework import serializers
from .models import AgendamentoDoacao
from accounts.models import User
from point.models import PontoColeta
from accounts.serializers import UserSerializer
from point.serializers import PontoColetaSerializer

class AgendamentoDoacaoSerializer(serializers.ModelSerializer):
    doador_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='doador')
    ponto_coleta_id = serializers.PrimaryKeyRelatedField(queryset=PontoColeta.objects.all(), source='ponto_coleta')

    class Meta:
        model = AgendamentoDoacao
        fields = ['id', 'doador', 'doador_id', 'ponto_coleta', 'ponto_coleta_id', 'data_hora_agendada', 'status']
        read_only_fields = ['doador', 'ponto_coleta']

    def create(self, validated_data):
        doador = validated_data.pop('doador')
        ponto_coleta = validated_data.pop('ponto_coleta')
        
        agendamento_doacao = AgendamentoDoacao.objects.create(doador=doador, ponto_coleta=ponto_coleta, **validated_data)
        
    
        return agendamento_doacao
    
    
        
