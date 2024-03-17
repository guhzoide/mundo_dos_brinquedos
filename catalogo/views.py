import os
from django.shortcuts import render
from catalogo.models import Brinquedos, Contatos, QuemSomos, FotosDiversas

def index(request):
    brinquedos = Brinquedos.objects.order_by("data_cadastro").filter(publicada=True)
    return render(request, 'catalogo/index.html', {"cards": brinquedos})

def fotos(request):
    fotos = FotosDiversas.objects.all()
    return render(request, 'catalogo/fotos.html', {"fotos": fotos})

def contatos(request):
    contato = Contatos.objects.order_by("nome").filter(publicada=True)
    return render(request, 'catalogo/contatos.html', {"contatos": contato})

def quem_somos(request):
    texto = QuemSomos.objects.all()
    return render(request, 'catalogo/quem_somos.html', {"texto": texto})

def descricao(request, brinquedo_id):
    descricao = Brinquedos.objects.filter(id=brinquedo_id)
    contato = Contatos.objects.order_by("nome").filter(publicada=True)
    return render(request, 'catalogo/descricao.html', {"descricao": descricao, "contatos":contato})