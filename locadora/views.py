from django.shortcuts import render, get_object_or_404, redirect
from locadora.models import Cliente, Veiculo, Locacao
from locadora.forms import LocacaoForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

#FUNÇÕES DE LISTAGEM DO SISTEMA
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'locadora/listar_clientes.html', {'clientes':clientes})

def listar_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'locadora/listar_veiculos.html', {'veiculos':veiculos})

def listar_locacoes(request):
    locacoes = Locacao.objects.all()
    return render(request, 'locadora/listar_locacoes.html', {'locacoes':locacoes})



def detalhar_locacao(request, id):
    locacao = get_object_or_404(Locacao, pk=id)
    return render(request, 'locadora/detalhar_locacao.html', {'locacao':locacao})


#FUNÇÃO CADASTRO NO SISTEMA
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


#FUNÇÕES DE EDIÇÃO NO SISTEMA
def editar_locacao(request, id):
    locacao = get_object_or_404(Locacao, pk=id)
    if request.method == "POST":
        form = LocacaoForm(request.POST, request.FILES, instance=locacao)
        if form.is_valid():
            locacao = form.save(commit=False)
            form.save()
            return redirect('detalhar_locacao', id=locacao.id)
    else:
        form = LocacaoForm(instance=locacao)
    return render(request, 'locadora/editar_locacao.html', {'form': form})


def editar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, pk=id)
    if request.method == "POST":
        form = VeiculoForm(request.POST, request.FILES, instance=veiculo)
        if form.is_valid():
            veiculo = form.save(commit=False)
            form.save()
            return redirect('detalhar_veiculo', id=veiculo.id)
    else:
        form = VeiculoForm(instance=veiculo)
    return render(request, 'locadora/editar_veiculo.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            form.save()
            return redirect('detalhar_cliente', id=cliente.id)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'locadora/editar_cliente.html', {'form': form})


#FUNÇÃO BUSCA NO SISTEMA
def buscar_locacao(request):
    infor = request.POST['infor']
    locacoes = Locacao.objects.filter(nome__contains=infor)
    return render(request, 'locadora/listar_locacoes.html', {'locacoes':locacoes})


def buscar_veiculo(request):
    infor = request.POST['infor']
    veiculos = Veiculo.objects.filter(nome__contains=infor)
    return render(request, 'locadora/listar_veiculos.html', {'veiculos':veiculos})


#FUNÇÃO DE LOGIN / ENTRAR NO SISTEMA
def page_login(request):
    return render(request, 'locadora/login.html',{})


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

#FUNÇÃO DE SAIR DO SISTEMA
def logout_usuario(request):
    logout(request)
    return render(request, 'locadora/login.html',{})



#FUNÇÕES DE DELEÇÃO
def delete_locacao(request, id):
    locacao = get_object_or_404(Locacao, pk=id)
    locacao.delete()
    return render(request,'locadora/listar_locacoes.html',{'locacao':locacao})


def delete_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, pk=id)
    veiculo.delete()
    return render(request,'locadora/listar_veiculos.html',{'veiculo':veiculo})


def delete_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    return render(request,'locadora/listar_clientes.html',{'cliente':cliente})