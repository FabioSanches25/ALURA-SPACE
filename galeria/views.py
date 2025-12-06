from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.all()
    # dados = {
    # 1: {"nome": "Nebulosa de Carina",
    #     "Legenda": "webbtelescope.org / NASA / James Webb"},
    # 2: {"nome": "Galáxia NGC 1079",
    #     "Legenda": "nasa.org / NASA  / Hubble"}
    # }
    return render(request, 'galeria/index.html',{"cards": fotografias})



def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html',{"fotografia": fotografia })




