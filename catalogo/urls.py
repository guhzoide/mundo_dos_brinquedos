from django.urls import path
from catalogo.views import *

urlpatterns = [
    path('', index, name='index'),
    path('fotos/', fotos, name='fotos'),
    path('contatos/', contatos, name='contatos'),
    path('quem_somos/', quem_somos, name='quem_somos'),
    path('descricao/<int:brinquedo_id>', descricao, name='descricao'),
]