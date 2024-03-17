from django.db import models
from datetime import datetime

class Brinquedos(models.Model):

    OPCOES_CATEGORIA = [
        ("INFLAVEL", "Infável"),
        ("CAMAELASTICA", "Cama elastica"),
        ("MESAS", "Mesas"),
        ("ELETRONICOS", "Eletrônicos"),
        ("PISCINABOLINHAS", "Piscina de bolinhas")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(max_length=500, null=False, blank=False, default="")
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    valor = models.FloatField(max_length=10, null=False, blank=False, default=0.00)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=False)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
class Contatos(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False, default=None)
    gmail = models.CharField(max_length=50, null=False, blank=False)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class QuemSomos(models.Model):
    titulo = models.CharField(max_length=6, null=False, blank=False, default="titulo")
    texto = models.TextField(max_length=1000, null=False, blank=False, default="") 

    def __str__(self):
        return self.titulo

class FotosDiversas(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    foto = models.ImageField(upload_to=f"fotos_diversas/%Y/%m/%d/", blank=True)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=False)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    