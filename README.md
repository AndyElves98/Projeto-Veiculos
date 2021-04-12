# Projeto-Veiculos
Sistema de Controle de Veiculos


# Descrição
O sistema foi implementado usando a linguagem de programação Python de alto nível, interpretada em script, orientada a objetos, 
de tipagem forte e dinâmica, juntamente com o framework Django, que é utilizado para o desenvolvimento web, escrito em Python, 
utilizando o padrão model – template - view. O uso deste sistema foi pensado inicialmente para controle de usuários sobre a locação
de veiculos. Ademais, durante o desenvolvimento, surgiu o pensamento futuro de se implementar algo que pode ser utilizado por todo 
público, por meio de um sistema de cadastro.
Para a melhor entender o funcionamento do sistema, do uso e benefícios no desenvolvimento desse software, buscou-se apresentar a maior interação, 
disponibilidade que o sistema proporciona para as partes interessadas.. Trata-se do desenvolvimento de um sistema de inserção,alteração, 
exclusão e listagem de veículos, clientes e locações.


# Projeto Web_Veiuculos

Para criação da app, criou-se uma pasta com o nome que dá referência a aplicação. Utilizando o Prompt de Comando, durante a configuração e depois 
no desenvolvimento de todo o projeto.


# Criação da Pasta do Projeto

```
$ mkdir web_veiculos

$ cd web_veiculos
```

Instalando o framework Django:🔧

```
(web_veiculos) ~$ python -m pip install --upgrade pip

(web_veiculos) ~$ pip install django
```


# Criando o projeto Django Veiculos 🚀

Dentro da pasta executa-se o seguinte comando:

```django-admin startproject core . ```

```django-admin``` é um script que criará os diretórios e arquivos para você. No diretório core (núcleo) do projeto será criada uma estrutura de diretórios.



# Criando um banco de dados para o Projeto

```python manage.py migrate ```

Comando para startar o servidor do Django:

``` python manage.py runserver ```



# Criando aplicação

``` python manage.py startapp locadora```

Depois de criar uma aplicação, também precisamos dizer ao Django que ele deve usá-la. 
Fazemos isso no arquivo core/settings.py -- abra-o no seu editor de código. Precisamos 
encontrar o INSTALLED_APPS e adicionar uma linha com 'livraria', logo acima do ].
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'locadora',
		]
```


# Criando os modelos para o Projeto

```
from django.db import models
from django.conf import settings

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=25)

    def __str__(self):
        return self.nome 

class Veiculo(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='locadora/media', blank=True)
    descricao = models.TextField()
    valor = models.IntegerField()

    def __str__(self):
        return self.nome 

class Locacao(models.Model):
    descricao = models.CharField(max_length=200)
    cliente = models.ManyToManyField(Cliente, blank = True) #relacionamento m-n muito-para-muitos
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name="Veiculo") #relacionamento 1-n
    placa = models.CharField(max_length=20)
    data = models.CharField(max_length=20)
    hora = models.CharField(max_length=20)
    #python -m pip install Pillow
    periodo = models.IntegerField()

    def __str__(self):
        return self.descricao
```

Para que possa enviar imagens, é necessário instalar a biblioteca Pillow com o comando:

```python -m pip install Pillow```


# Criando tabelas para nossos modelos no banco de dados

```python manage.py makemigrations locadora```

O Django preparou um arquivo de migração que precisamos aplicar para o banco de dados.

```python manage.py migrate livraria```


# Django Admin

Para fazer as operações de

 - Adicionar
 - Editar
 - Deletar

Nas tabelas Cliente, Veiculo e Locação que modelamos iremos inicialmente usar o admin do Django. 
Abrindo o arquivo locadora/admin.py no editor de código e acrescentou-se os códigos seguintes:
```
from django.contrib import admin
from .models import Cliente, Veiculo, Locacao

Register your models here.

admin.site.register(Cliente)
admin.site.register(Veiculo)
admin.site.register(Locacao)
```

Vamos startar o servidor web, e dar uma olhada

```python manage.py runserver```

Vamos acessar a área do administrador do sistema do framework Django, copiando endereço no navegador:

```http://127.0.0.1:8000/admin/```

Para fazer login, será criado um superusuário (superuser) - uma conta de usuário que pode controlar tudo no site.

``` python manage.py createsuperuser ```

Ao ser solicitado, preencho o nome de usuário, email e senha.


# URLs

Uma URL é um endereço da web. Você pode ver uma URL toda vez que você visita um website - 
ela aparece na barra de endereços do seu navegador. (Sim! 127.0.0.1:8000 é uma URL! E https://djangogirls.org também é uma URL.)


# Funcionamento das URLs no Django

```
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

```

# Criando locadora.urls

```
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.listar_locacoes, name='listar_locacoes'),
```

Agora atribui-se uma view chamada listar_locações à URL raiz. Este padrão de URL corresponde a uma sequência de caracteres vazia,
e o resolvedor de URLs do Django irá ignorar o nome de domínio (ou seja, http://127.0.0.1:8000 /) que antecede o caminho completo da URL.


# Django views

Uma view é o lugar onde é colocada a "lógica" da nossa aplicação. Ela vai extrair informações do model que foi criado e entregá-las a um template.
 
 ```
from django.shortcuts import render

def listar_locações(request):
    return render(request, 'locadora/listar_locacoes.html', {})

```

Será criado um arquivo listar_locacoes.html.Mas antes cria-se também a pasta locadora\templates, em seguida crie um diretório chamado locadora.

- locadora
	- templates
  		- locadora
				- listar_locacoes.html


# Dados dinâmicos em templates

```
from django.shortcuts import render
from locadora.models import Cliente, Veiculo, Locacao

def listar_clientes(request):
    return render(request, 'locadora/listar_clientes.html', {'clientes':clientes})

def listar_veiculos(request):
    return render(request, 'locadora/listar_veiculos.html', {'veiculos':veiculos})

def listar_locacoes(request):
    return render(request, 'locadora/listar_locacoes.html', {'locacoes':locacoes})
```

Cria-se arquivos HTML na pasta locadora/templates/locadora.

```
listar_veiculos.html
listar_clientes.html
```

É necessário criar também três novas rotas no arquivo locadora/urls.py

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_locacoes, name='listar_locacoes'),
    path('listar_clientes', views.listar_clientes, name='listar_clientes'), 
    path('listar_veiculos', views.listar_veiculos, name='listar_veiculos'), 
    ]
 ```
 
 
# QuerySet

QuerySets e seu funcionamento:

```
from django.shortcuts import render
from locadora.models import Cliente, Veiculo, Locacao

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'locadora/listar_clientes.html', {'clientes':clientes})

def listar_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'locadora/listar_veiculos.html', {'veiculos':veiculos})

def listar_locacoes(request):
    locacoes = Locacao.objects.all()
    return render(request, 'locadora/listar_locacoes.html', {'locacoes':locacoes})
```


# Templates para lista de Clientes, Veiculos e Locacoes

```
<html>
    <head>
        <title>Django Locadora</title>
    </head>
    <body>
        <h3>Lista dos Clientes</h3>
        {{clientes}}
    </body>
</html>

```


# Pagina Principal - Listar Locações

```
<html>
    <head>
        <title>Django Locadora</title>
    </head>
    <body>
    <center><h3>Locações Solicitadas</h3></center>

		         {% for locacao in locacoes %}
				          Descricao: {{ locacao.descricao }}<br>
				          Cliente: <br/>
				          {% for nome in locacao.cliente.all %}
				              {{ nome }}<br/></h5>
				          {% endfor %}
				          {% for nome in locacao.veiculo.all %}
				              {{ nome }}<br/></h5>
				          {% endfor %}
				          Placa: {{ locacao.placa }}<br/>
				          Data: {{ locacao.data }}<br/>
				          Hora: {{ locacao.Hora }}<br/>
				          Período: {{ locacao.periodo }}<br/>
		        {% endfor %}
    </body>
</html>
```

# Listagem de Clientes

```
<html>
    <head>
    </head>
    <body>
    <center><h3>Lista de Clientes</h3></center>
             {% for cliente in clientes %}
                    <td>
                        Nome Completo: {{ cliente.nome }}<br/>
                        CPF: {{ cliente.cpf }}<br/> 
                    </td>
            {% endfor %}
    </body>
</html> 
```

# Lista de Veiculos

``` 
<html>
    <head>
        <title>Django Locadora</title>
    </head>
    <body>
           {% for veiculo in veiculos %}
                  Nome: {{ veiculo.nome }}<br>
                  <img height="300" width="400" src="{{ veiculo.imagem.url }}">
                  Descricao: {{ veiculo.descricao }}<br/>
                  Valor: {{ veiculo.valor }}<br/>
                  <br>
    </body>
</html> 
```

# Estendendo os templates

Outra coisa boa que o Django tem para você é o template extending - extensão de templates.
O que isso significa? Significa que você pode usar as mesmas partes do seu HTML em diferentes páginas do seu site.


# Criando um template base

Vamos criar um arquivo base.html na pasta locadora/templates/locadora/:


``` 
{% load static %}

<!doctype html>
<html lang="en">
    <head> 
    
<main class="container">
  <div class="bg-light p-5 rounded">
      {% block content %}
        
      {% endblock %}
  </div>
</main> 
```

O arquivo locadora/templates/locadora/listar_locacoes.html fica agora da seguinte forma:

```
{% extends 'locadora/base.html' %}

{% block content %}
    <h1>Lista de Locações</h1>
        {% for locacoes in locacoes %}
            <h5>Descricao: {{ locacao.descricao }}<br/></h5>
				            <h5>Cliente: <br/></h5>
				            <h5>{% for nome in locacao.cliente.all %}</h5>
				            <h5>    {{ nome }}<br/></h5>
				            {% endfor %}
				            <h5>{% for nome in locacao.veiculo.all %}</h5>
				            <h5>    {{ nome }}<br/></h5>
				            {% endfor %}
				            <h5>Placa: {{ locacao.placa }}<br/></h5>
				            <h5>Data: {{ locacao.data }}<br/></h5>
				            <h5>Hora: {{ locacao.Hora }}<br/></h5>
				            <h5>Período: {{ locacao.periodo }}<br/></h5>
				            <br>
            {% endfor %}     
            <br>
        {% endfor %}
{% endblock %}
```


# Formulários do Django

Por último, será feito uma forma legal de adicionar e editar os locações casdastrados no sistema

```
from django import forms
from locadora.models import Locacao

class LocacaoForm(forms.ModelForm):

    class Meta:
        model = Locacao
        fields = ('descricao','cliente','veiculo','placa', 
        'data', 'hora', 'periodo')

        widgets = {
            'descricao': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Ex: veiculo pouco usado'}),
            'cliente': forms.SelectMultiple(attrs={ 'class': 'form-control'}),
            'veiculo': forms.Select(attrs={ 'class': 'form-control'}),
            'placa': forms.TextInput(attrs={ 'class': 'form-control'}),
            'data': forms.TextInput(attrs={ 'class': 'form-control'}),
            'hora': forms.TextInput(attrs={ 'class': 'form-control'}),
            'periodo': forms.TextInput(attrs={ 'class': 'form-control',
                                            'placeholder':'Ex: Tempo que pretende usar'}),
        }
```


# Link para a página com o formulário

Criar um link para o menu que leverá para a página que contém o formulário para cadastrar as locações.

No arquivo locadora/templates/locadra/base.html em um dos nossos links do menu iremos adicionar o seguinte techo de código.

```
<li class="nav-item">
          <a class="nav-link" href="{% url 'cadastrar_locacao' %}">Cadastrar Locação</a>
    </li>
```

# Criando a nova URL

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_locacoes, name='listar_locacoes'),
    path('listar_clientes', views.listar_clientes, name='listar_clientes'), #nova url
    path('listar_veiculos', views.listar_veiculos, name='listar_veiculos'), #nova url
    path('locacao/<int:id>/', views.detalhar_locacao, name='detalhar_locacao'), #nova url
    path('locacao/new/', views.cadastrar_locacao, name='cadastrar_locacao'), #nova url
```


# Criando a Template editar_locacao.html


Vamos criar o arquivo locadora/templates/locadora/editar_locacao.html


``` 
{% extends 'locadora/base.html' %}

{% block content %}
    <h2>Nova Locação</h2>
    <form method="POST" class="table" enctype="multipart/form-data">
    {% csrf_token %}
        <div class="form-group">
            {{ form.as_p }}
         </div>
        <button type="submit" class="save btn btn-default">Save</button>
    </form>
{% endblock %} 
```

# Salvando os dados do formulário

Vamos abrir o arquivo ```locadora/views.py``` e alterar a nossa nova função no arquivo.

```
from django.shortcuts import render, get_object_or_404, redirect
from locadora.models import Cliente, Veiculo, Locacao
from locadora.forms import LocacaoForm

def cadastrar_locacao(request):
    if request.method == "POST":
        form = LocacaoForm(request.POST, request.FILES)
        if form.is_valid():
            locacao = form.save(commit=False)
            form.save()
            return redirect('detalhar_locacao', id=locacao.id)
    else:
        form = LocacaoForm()
    return render(request, 'locadora/editar_locacao.html', {'form': form})
```


# Editando as informações da locação

```
{% extends 'locadora/base.html' %}
{% block content %}
    <table class="table">
        {% for locacoes in locacoes %}
            <tr>
                <td>
                <h5>Descricao: {{ locacao.descricao }}<br/></h5>
				            <h5>Cliente: <br/></h5>
				            <h5>{% for nome in locacao.cliente.all %}</h5>
				            <h5>    {{ nome }}<br/></h5>
				            {% endfor %}
				            <h5>{% for nome in locacao.veiculo.all %}</h5>
				            <h5>    {{ nome }}<br/></h5>
				            {% endfor %}
				            <h5>Placa: {{ locacao.placa }}<br/></h5>
				            <h5>Data: {{ locacao.data }}<br/></h5>
				            <h5>Hora: {{ locacao.Hora }}<br/></h5>
				            <h5>Período: {{ locacao.periodo }}<br/></h5>
				            <br>
				            <br>
				            <td>
				                <a class="btn btn-default" href="{% url 'editar_locacao' id=locacao.id %}">
				                    <button type="button" class="btn btn-danger">Editar / Alterar</button>
				                </a>
				            </td>
				        </td>
				    </tr>
		        {% endfor %}
			</table>
	    {% endblock %}
    </body>
</html>
```


# Criando a nova URL editar_locacao

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_locacoes, name='listar_locacoes'),
    path('listar_clientes', views.listar_clientes, name='listar_clientes'), #nova url
    path('listar_veiculos', views.listar_veiculos, name='listar_veiculos'), #nova url
    path('locacao/<int:id>/', views.detalhar_locacao, name='detalhar_locacao'), #nova url
    path('locacao/new/', views.cadastrar_locacao, name='cadastrar_locacao'), #nova url
    path('locacao/editar/<int:id>/', views.editar_locacao, name='editar_locacao'),#nova url
```

Agora é startar o servidor e vermos os resultados.

``` python manage.py ```


# Buscando locações na locadora

Vamos começar com a edição de um link dentro do arquivo locadora/templates/locadora/base.html. 
Abra-o no editor de código e deixe ele dessa forma:

```
<form class="d-flex" action="{% url 'buscar_livro' %}" method="POST">
      {% csrf_token %}
        <input name="infor" class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
</form>
```

# Criando a nova URL buscar_veiculo

```
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.listar_locacoes, name='listar_locacoes'),
    path('listar_clientes', views.listar_clientes, name='listar_clientes'), #nova url
    path('listar_veiculos', views.listar_veiculos, name='listar_veiculos'), #nova url
    path('locacao/<int:id>/', views.detalhar_locacao, name='detalhar_locacao'), #nova url
    path('locacao/new/', views.cadastrar_locacao, name='cadastrar_locacao'), #nova url
    path('locacao/editar/<int:id>/', views.editar_locacao, name='editar_locacao'),#nova url
		path('cliente/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),#nova url
    path('veiculo/editar/<int:id>/', views.editar_veiculo, name='editar_veiculo'),#nova url
    path('buscar_locacao', views.buscar_locacao, name='buscar_locacao'),#nova url
    path('buscar_veiculo', views.buscar_veiculo, name='buscar_veiculo'),#nova url
    
 ```
 
 
 # Criando a view buscar_veiculo
 
 ```
 def buscar_veiculo(request):
    infor = request.POST['infor']
    veiculos = Veiculo.objects.filter(nome__contains=infor)
    return render(request, 'locadora/listar_veiculos.html', {'veiculos':veiculos})
 ```
 
 
 # Deletando as locações
 
 Para iniciar. No ```listar_locações.html``` adicionaremos o botão para a deleção.
 
 ```
 {% extends 'locadora/base.html' %}

<html>
    <head>
        <title>Django Locadora</title>
    </head>
    <body>
    {% block content %}
    {% if user.is_authenticated %}
        <center><h3>Bem Vindo, Usuário: {{user.username}}, Orientamos que vá para a guia "Lista de Veiculos"</h3></center>
        <br>
    {% else %}
        <h3><p>Você ainda não fez o login, por favor realiaze o login, para que possa usufruir das atribuições do sistema</p></h3>
    {% endif %}
    <center><h3>Locações Solicitadas</h3></center>
		    <table class="table">
		         {% for locacao in locacoes %}
		         	<tr>
		         		<br>
		         		<td>
				            <h5>Descricao: {{ locacao.descricao }}<br/></h5>
				            <h5>Cliente: <br/></h5>
				            <h5>{% for nome in locacao.cliente.all %}</h5>
				            <h5>    {{ nome }}<br/></h5>
				            {% endfor %}
				            <h5>{% for nome in locacao.veiculo.all %}</h5>
				            <h5>    {{ nome }}<br/></h5>
				            {% endfor %}
				            <h5>Placa: {{ locacao.placa }}<br/></h5>
				            <h5>Data: {{ locacao.data }}<br/></h5>
				            <h5>Hora: {{ locacao.Hora }}<br/></h5>
				            <h5>Período: {{ locacao.periodo }}<br/></h5>
				            <br>
				            <br>
				            <td>
				                <a class="btn btn-default" href="{% url 'editar_locacao' id=locacao.id %}">
				                    <button type="button" class="btn btn-danger">Editar / Alterar</button>
				                </a>
				            </td>
				            <td>
				                <a class="btn btn-default" href="{% url 'delete_locacao' id=locacao.id %}">
				                    <button type="button" class="btn btn-danger">Apagar</button>
				                </a>
				            </td>
				        </td>
				    </tr>
		        {% endfor %}
			</table>
	    {% endblock %}
    </body>
</html>
```

# Criando a nova URL delete_locacao

```
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.listar_locacoes, name='listar_locacoes'),
    path('listar_clientes', views.listar_clientes, name='listar_clientes'), #nova url
    path('listar_veiculos', views.listar_veiculos, name='listar_veiculos'), #nova url
    path('locacao/<int:id>/', views.detalhar_locacao, name='detalhar_locacao'), #nova url
    path('locacao/new/', views.cadastrar_locacao, name='cadastrar_locacao'), #nova url
    path('locacao/editar/<int:id>/', views.editar_locacao, name='editar_locacao'),#nova url
		path('cliente/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),#nova url
    path('veiculo/editar/<int:id>/', views.editar_veiculo, name='editar_veiculo'),#nova url
    path('buscar_locacao', views.buscar_locacao, name='buscar_locacao'),#nova url
    path('locacao/deletar/<int:id>/', views.delete_locacao, name='delete_locacao'),
    path('page_login', views.page_login, name='page_login'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),
]
```


# Criando a view para a deleção de locações

```
def delete_locacao(request, id):
    locacao = get_object_or_404(Locacao, pk=id)
    locacao.delete()
    return render(request,'locadora/listar_locacoes.html',{'locacao':locacao})
```
 
 
 # Login e logout do sistema locadora
 
 ```
     <form class="d-flex" action="{% url 'buscar_veiculo' %}" method="POST">
      {% csrf_token %}
        <input name="infor" class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
      <ul class="nav justify-content-end">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="{% url 'page_login' %}">Login</a>
        </li>
      </ul>
 ```
 
#  Criando a nova URL page_login

```
from django.urls import path
from . import views #arquivo views que ainda não utilizamos

urlpatterns = [
    path('', views.listar_locacoes, name='listar_locacoes'),
    path('listar_clientes', views.listar_clientes, name='listar_clientes'), #nova url
    path('listar_veiculos', views.listar_veiculos, name='listar_veiculos'), #nova url
    path('locacao/<int:id>/', views.detalhar_locacao, name='detalhar_locacao'), #nova url
    path('locacao/new/', views.cadastrar_locacao, name='cadastrar_locacao'), #nova url
    path('locacao/editar/<int:id>/', views.editar_locacao, name='editar_locacao'),#nova url
		path('cliente/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),#nova url
    path('veiculo/editar/<int:id>/', views.editar_veiculo, name='editar_veiculo'),#nova url
    path('buscar_locacao', views.buscar_locacao, name='buscar_locacao'),#nova url
    path('buscar_veiculo', views.buscar_veiculo, name='buscar_veiculo'),#nova url
    path('page_login', views.page_login, name='page_login'),
```

# Criando a view page_login

No arquivo locadora/views.py e adicionar a nova função no arquivo

```
def page_login(request):
    return render(request, 'locadora/login.html',{})

```

# Criando o formulário de login

```
% extends 'locadora/base.html' %}
{% block content %}
    <form action="{% url 'autenticar_usuario' %}" method="post">
    {% csrf_token %}
        <div class="mb-3" >
            <label for="exampleInputEmail1" class="form-label">Username</label>
            <input name="username" type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">Password</label>
            <input name="password" type="password" class="form-control" id="exampleInputPassword1">
        </div>
    <button type="submit" class="btn btn-primary">Login</button>
    </form>
{% endblock %}
```

# Criando a rota para autenticação do usuário

 A rota de autenticação do usuário ao sistema, essa rota redirecionará o os dados do usuário para a nossa 
 função que teremos no view.py chamada de autenticar_usuario.

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_locacoes, name='listar_locacoes'),
    path('listar_clientes', views.listar_clientes, name='listar_clientes'), #nova url
    path('listar_veiculos', views.listar_veiculos, name='listar_veiculos'), #nova url
    path('locacao/<int:id>/', views.detalhar_locacao, name='detalhar_locacao'), #nova url
    path('locacao/new/', views.cadastrar_locacao, name='cadastrar_locacao'), #nova url
    path('locacao/editar/<int:id>/', views.editar_locacao, name='editar_locacao'),#nova url
		path('cliente/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),#nova url
    path('veiculo/editar/<int:id>/', views.editar_veiculo, name='editar_veiculo'),#nova url
    path('buscar_locacao', views.buscar_locacao, name='buscar_locacao'),#nova url
    path('buscar_veiculo', views.buscar_veiculo, name='buscar_veiculo'),#nova url
    path('locacao/deletar/<int:id>/', views.delete_locacao, name='delete_locacao'),
    path('veiculo/deletar/<int:id>/', views.delete_veiculo, name='delete_veiculo'),
    path('cliente/deletar/<int:id>/', views.delete_cliente, name='delete_cliente'),

     #rotas do login e logout
    path('page_login', views.page_login, name='page_login'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
 
 ```
 
 # Criando a view autenticar_usuario
 
 No arquivo ```locadora/views.py``` e adicionar a nova função no arquivo. Essa função irá verificar os dados do usuário, 
 se ele realmente está cadastrado no sistema utilizando a função ```authenticate``` e ```login```.
 
 Resumidamente a função ```authenticate``` ela realiza uma busca no banco no model User e verifica se os dados do usuário
 são válidos. A função ```login``` você irá apontar esse usuário para sessão atual do navegador para o sistema.

```
from django.shortcuts import render, get_object_or_404, redirect
from locadora.models import Cliente, Veiculo, Locacao
from locadora.forms import LocacaoForm
from django.contrib.auth import authenticate, login, logout

 def autenticar_usuario(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        locacoes = Locacao.objects.all()
        return render(request, 'locadora/listar_locacoes.html', {'locacoes':locacoes})
    else:
        return render(request, 'locadora/login.html',{})
```

# Criando o logout

```
{% extends 'locadora/base.html' %}

<html>
    <head>
        <title>Django Locadora</title>
    </head>
    <body>
    {% block content %}
    {% if user.is_authenticated %}
        <center><h3>Bem Vindo, Usuário: {{user.username}}, Orientamos que vá para a guia "Lista de Veiculos"</h3></center>
        <br>
    {% else %}
        <h3><p>Você ainda não fez o login, por favor realiaze o login, para que possa usufruir das atribuições do sistema</p></h3>
    {% endif %}
    <center><h3>Locações Solicitadas</h3></center>
		    <table class="table">
		         {% for locacao in locacoes %}
		         	<tr>
		         		<br>
		         		<td>
				            <h5>Descricao: {{ locacao.descricao }}<br/></h5>
				            <h5>Cliente: <br/></h5>
				            <h5>{% for nome in locacao.cliente.all %}</h5>
				            <h5>    {{ nome }}<br/></h5>
				            {% endfor %}
				            <h5>{% for nome in locacao.veiculo.all %}</h5>
				            <h5>    {{ nome }}<br/></h5>
				            {% endfor %}
				            <h5>Placa: {{ locacao.placa }}<br/></h5>
				            <h5>Data: {{ locacao.data }}<br/></h5>
				            <h5>Hora: {{ locacao.Hora }}<br/></h5>
				            <h5>Período: {{ locacao.periodo }}<br/></h5>
				            <br>
				            <br>
				            <td>
				                <a class="btn btn-default" href="{% url 'editar_locacao' id=locacao.id %}">
				                    <button type="button" class="btn btn-danger">Editar / Alterar</button>
				                </a>
				            </td>
				            <td>
				                <a class="btn btn-default" href="{% url 'delete_locacao' id=locacao.id %}">
				                    <button type="button" class="btn btn-danger">Apagar</button>
				                </a>
				            </td>
				        </td>
				    </tr>
		        {% endfor %}
			</table>
	    {% endblock %}
    </body>
</html>

```

# Criando a nova URL logout_usuario

 No ```locadora/urls.py``` e adicionar a nova rota do nosso sistema. Essa nota irá redirecionar para a função de logout do sistema,
 onde será excluído os dados de sessão do usuário do navegador.
 
 ```
 from django.urls import path
from . import views #arquivo views que ainda não utilizamos

urlpatterns = [
    path('', views.listar_locacoes, name='listar_locacoes'),
    path('listar_clientes', views.listar_clientes, name='listar_clientes'), #nova url
    path('listar_veiculos', views.listar_veiculos, name='listar_veiculos'), #nova url
    path('locacao/<int:id>/', views.detalhar_locacao, name='detalhar_locacao'), #nova url
    path('locacao/new/', views.cadastrar_locacao, name='cadastrar_locacao'), #nova url
    path('locacao/editar/<int:id>/', views.editar_locacao, name='editar_locacao'),#nova url
		path('cliente/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),#nova url
    path('veiculo/editar/<int:id>/', views.editar_veiculo, name='editar_veiculo'),#nova url
    path('buscar_locacao', views.buscar_locacao, name='buscar_locacao'),#nova url
    path('buscar_veiculo', views.buscar_veiculo, name='buscar_veiculo'),#nova url
    path('locacao/deletar/<int:id>/', views.delete_locacao, name='delete_locacao'),
    path('veiculo/deletar/<int:id>/', views.delete_veiculo, name='delete_veiculo'),
    path('cliente/deletar/<int:id>/', views.delete_cliente, name='delete_cliente'),

     #rotas do login e logout
    path('page_login', views.page_login, name='page_login'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),
]
```

# Criando a view logout_usuario

```
def logout_usuario(request):
    logout(request)
    return render(request, 'locadora/login.html',{})
    
```

# Melhorando o visual do sistema de login e logout

```
 <form class="d-flex" action="{% url 'buscar_livro' %}" method="POST">
      {% csrf_token %}
        <input name="infor" class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
      <ul class="nav justify-content-end">
        <li class="nav-item">
        {% if user.is_authenticated %}
          <a class="nav-link active" aria-current="page" href="{% url 'logout_usuario' %}">Sair</a>
        {% else %}
          <a class="nav-link active" aria-current="page" href="{% url 'page_login' %}">Login</a>
        {% endif %}
        </li>
      </ul>
   ```
   
