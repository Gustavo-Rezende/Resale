from django.shortcuts import render
from rest_framework import viewsets
from .models import Imoveis
from .serializers import ImoveisSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class ImoveisViewSet(viewsets.ModelViewSet):
    queryset = Imoveis.objects.all()
    serializer_class = ImoveisSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id', 'Nome']

