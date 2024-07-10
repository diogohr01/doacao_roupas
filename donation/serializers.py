from rest_framework import serializers
from .models import AgendamentoDoacao
from accounts.models import User
from point.models import PontoColeta
from accounts.serializers import UserSerializer
from point.serializers import PontoColetaSerializer
from catalog.serializers import CatalogoRoupasSerializer
import os
#from twilio.rest import Client


class AgendamentoDoacaoSerializer(serializers.ModelSerializer):
    doador_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='doador')
    ponto_coleta_id = serializers.PrimaryKeyRelatedField(queryset=PontoColeta.objects.all(), source='ponto_coleta')
    
    class Meta:
        model = AgendamentoDoacao
        fields = ['id', 'doador', 'doador_id','catalog','quantidade', 'ponto_coleta', 'ponto_coleta_id', 'data_hora_agendada', 'status']
        read_only_fields = ['doador', 'ponto_coleta']


    def create(self, validated_data):
        doador = validated_data.pop('doador')
        ponto_coleta = validated_data.pop('ponto_coleta')
        data_hora_agendada = validated_data.get('data_hora_agendada')
        
        if doador.is_doador == True:
            if AgendamentoDoacao.objects.filter(data_hora_agendada=data_hora_agendada).exists():
                raise serializers.ValidationError({'non_field_errors': 'Já existe uma doação nesse horário, por favor escolha outro momento para podermos seguir com a busca.'})
            
        # Cria o agendamento da doação
        
        agendamento_doacao = AgendamentoDoacao.objects.create(doador=doador, ponto_coleta=ponto_coleta, **validated_data)
        
       
        
        
        '''
        from_whatsapp_number = 'whatsapp:+14155238886'
        to_whatsapp_number = 'whatsapp:+555197450106'
        
        if doador.is_doador == True:
            mensagem = (f"Olá, um novo pedido de doação foi agendado:\n"
                    f"Pedido numero: {agendamento_doacao.id}\n"
                    f"Doador: {doador.name}\n"
                    f"Endereço: {ponto_coleta.endereco}, {ponto_coleta.cidade}, {ponto_coleta.estado}\n"
                    f"Data e Hora Agendada: {agendamento_doacao.data_hora_agendada}\n"
                    f"Status: {agendamento_doacao.status}")
        
        else:
            mensagem = (
                        f"Olá, um novo pedido de beneficiário foi agendado:\n"
                        f"Pedido numero: {agendamento_doacao.id}\n"
                        f"Beneficiario: {doador.name}\n"
                        f"Endereço: {ponto_coleta.endereco}, {ponto_coleta.cidade}, {ponto_coleta.estado}\n"
                        f"Data e Hora Agendada: {agendamento_doacao.data_hora_agendada}\n"
                        f"Status: {agendamento_doacao.status}\n"
                        f"Roupas: {agendamento_doacao.catalog.tipo} ({agendamento_doacao.catalog.tamanho}) - {agendamento_doacao.catalog.condicao}\n"
                        f"Quantidade: {agendamento_doacao.quantidade}"
)
        
        client.messages.create(body=mensagem,
                               from_=from_whatsapp_number,
                               to=to_whatsapp_number)
        
        '''
        
    
        return agendamento_doacao
    
    
        
