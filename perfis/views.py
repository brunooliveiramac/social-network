from django.shortcuts import render
from perfis.models import Perfil


def index(request):
    return render(request, 'index.html', { 'perfis' : Perfil.objects.all()})

def exibir(request, id):
    perfil = Perfil.objects.get(id=id)
    return render(request, 'perfil.html', { "perfil" : perfil })

def convidar(request, id):
    perfil_a_convidar = Perfil.objects.get(id=id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return render(request, 'index.html', { 'perfis' : Perfil.objects.all()})

def get_perfil_logado(request):
   return Perfil.objects.get(id=1)     