from random import choice

frase = ['hello', 'hola', 'hi']

def basico(request):
    return {'titulo': choice(frase)}