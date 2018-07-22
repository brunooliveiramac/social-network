from django.shortcuts import render, redirect
from perfis.models import Perfil



def index(request):
    return render(request, 'index.html', { 'perfis' : Perfil.objects.all(), 'perfil_logado' : get_perfil_logado(request)})

def exibir(request, id):
    perfil = Perfil.objects.get(id=id)
    return render(request, 'perfil.html', { "perfil" : perfil })

def convidar(request, id):
    perfil_a_convidar = Perfil.objects.get(id=id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index');

def get_perfil_logado(request):
   return Perfil.objects.get(id=1)     