from django.contrib import admin
from catalogo.models import *


class ListandoBrinquedos(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "valor" , "categoria", "publicada", "data_cadastro")
    list_display_links = ("id", "nome")
    search_fields = ("id", "nome")
    list_filter = ("categoria", "publicada")
    list_per_page = 10


class ListandoContatos(admin.ModelAdmin):
    list_display = ("id", "nome", "numero", "gmail", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("id", "nome", "numero", "gmail")
    list_filter = ("publicada",)
    list_per_page = 10

class TextoQuemSomos(admin.ModelAdmin):
    list_display = ("id", "titulo")
    list_display_links = ("id", "titulo")

class ListandoFotosDiversas(admin.ModelAdmin):
    list_display = ("id", "nome", "data_cadastro", "publicada")
    list_display_links = ("id", "nome")
    list_filter = ("nome", "publicada")

admin.site.register(Brinquedos, ListandoBrinquedos)
admin.site.register(Contatos, ListandoContatos)
admin.site.register(QuemSomos, TextoQuemSomos)
admin.site.register(FotosDiversas, ListandoFotosDiversas)