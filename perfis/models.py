from django.db import models

class Perfil(models.Model): # Do not need init anymore

  nome = models.CharField(max_length=255, null=False)
  email = models.CharField(max_length=255, null=False)     
  telefone = models.CharField(max_length=15, null=False)
  nome_empresa = models.CharField(max_length=255, null=False)

  def convidar(self, perfil_convidado):
      pass