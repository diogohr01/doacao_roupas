from rest_framework import serializers
from catalog.models import CatalogoRoupas

class CatalogoRoupasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogoRoupas
        fields = ['id','tipo', 'tamanho', 'condicao', 'quantidade']

    def create(self, validated_data):
        tipo = validated_data.get('tipo')
        tamanho = validated_data.get('tamanho')
        condicao = validated_data.get('condicao')
        quantidade = validated_data.get('quantidade', 0)

        # Tentar buscar um registro existente com as mesmas características
        try:
            instance = CatalogoRoupas.objects.get(
                tipo=tipo,
                tamanho=tamanho,
                condicao=condicao
            )
            # Se encontrar, atualizar a quantidade
            instance.quantidade += quantidade
            instance.save()
            return instance
        except CatalogoRoupas.DoesNotExist:
            # Se não encontrar, criar um novo registro
            return super().create(validated_data)
