from rest_framework import serializers
from .models import Imoveis
from .models import Imobiliaria

class ImoveisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Imoveis
        fields = ['id', 'Nome', 'Endereco', 'Descricao', 'Status', 'Caracteristica', 'Tipo', 'Finalidade', 'Imobiliaria']


class ImobiliariaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Imobiliaria
        fields = ['id', 'Nome', 'Endereco']

