# social-network
sample application with Django

<b>Notes:</b>

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

python manage.py startapp

python manage.py shell

> from perfis.models import Perfil
> perfil = Perfil(nome='Joao', email='joao@joao.com', telefone='n/a', nome_empresa='Batata')
> perfil.save()
> perfil = Perfil(nome='Mbappe', email='mbappe@jogamuito.com', telefone='n/a', nome_empresa='France')
> perfil.save()


> from perfis.models import Convite, Perfil
> a_convidar = Perfil.objects.get(id=1)
> solicitante = Perfil.objects.get(id=2)
> solicitante.convidar(a_convidar)


