__author__ = 'santiago'

from random import choice

frases = [
    'leonidas esta sentado',
    'freddy se fue',
    'cristian esta arriba',
    'soy santiago'
]


def ejemplo(request):
    return {'frase': choice(frases)}

