from random import choice
from django.shortcuts import redirect

paises = ['Colombia', 'Peru', 'Mexico']

def de_donde_vengo(request):
    return choice(paises)

class PaisMiddleware():
    def process_request(self, request):
	pais = de_donde_vengo(request)
	if pais == 'Mexico':
	    return redirect('http://localhost:8000/tracks/Debaser/')