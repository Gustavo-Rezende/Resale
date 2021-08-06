from rest_framework import serializers
from .models import Imoveis

class ImoveisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Imoveis
        fields = ['id', 'Nome', 'Endereco', 'Descricao', 'Status', 'Caracteristica', 'Tipo', 'Finalidade', 'Imobiliaria']

