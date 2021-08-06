from django.db import models

STATUS_CHOICES = (
    ('Ativo', 'Ativo'),
    ('Inativo', 'Inativo'),
)

TIPO_CHOICES = (
    ('Apartamento', 'Apartamento'),
    ('Casa', 'Casa'),
)

FINALIDADE_CHOICES = (
    ('Residencial', 'Residencial'),
    ('Escritorio', 'Escritorio'),
)

class Imoveis(models.Model):
    Nome = models.CharField(max_length=50)
    Endereco = models.CharField(max_length=100)
    Descricao = models.CharField(max_length=100)
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    Caracteristica = models.CharField(max_length=200, blank=True)
    Tipo = models.CharField(max_length=15, choices=TIPO_CHOICES)
    Finalidade = models.CharField(max_length=20, blank=True, choices=FINALIDADE_CHOICES)
    Imobiliaria = models.CharField(max_length=30)

    def __str__(self):
        return self.Nome

