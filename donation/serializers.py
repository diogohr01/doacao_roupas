from rest_framework import serializers
from.models import AgendamentoDoacao
from accounts.serializers import UserSerializer
from point.serializers import PontoColetaSerializer


class AgendamentoDoacaoSerializer(serializers.ModelSerializer):

    doador = UserSerializer(read_only=True)

    ponto_coleta = PontoColetaSerializer(read_only=True)


    class Meta:

        model = AgendamentoDoacao

        fields = ['id', 'doador', 'ponto_coleta', 'data_hora_agendada', 'status']