__author__ = 'santiago'

from django.contrib import admin

from models import *


class EnlaceAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "enlace", "categoria", "imagen_voto", 'es_popular')
    list_filter = ("categoria", )
    search_fields = ('categoria__titulo',)
    list_editable = ("titulo", "enlace", 'categoria')
    raw_id_fields = ('categoria', 'usuario',)

    def imagen_voto(self, obj):
        url = obj.mis_votos_en_imagen_rosada()
        tag = '<img src="%s"/>' % url
        return tag

    imagen_voto.allow_tags = True
    imagen_voto.admin_irder_field = 'votos'


class EnlaceInline(admin.StackedInline):
    model = Enlace
    extra = 1


class CategoriaAdmin(admin.ModelAdmin):
    inlines = [EnlaceInline]


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Enlace, EnlaceAdmin)