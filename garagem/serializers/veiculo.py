from rest_framework import serializers
from garagem.models import Veiculo, Modelo, Acessorio, Cor
from garagem.serializers import ModeloSerializer, AcessorioSerializer

class VeiculoSerializer(serializers.ModelSerializer):
    modelo = ModeloSerializer()
    acessorios = AcessorioSerializer(many=True)
    cor = serializers.CharField(source='cor.nome')

    class Meta: 
        model = Veiculo
        fields = (
            'id',
            "preco",
            'modelo',
            'ano',
            'cor',
            "acessorios",
        )