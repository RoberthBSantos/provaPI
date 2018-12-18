from django.shortcuts import render, redirect, get_object_or_404
from .models import Empresas, Acao, Cotacao
from .forms import FormularioEmpresa, FormularioAcao, FormularioCotacao


def listar_empresas(request):
    empresas = Empresas.objects.all()
    return render(request, 'empresas.html', {'empresas' : empresas})

def listar_cotacoes(request):
    cotacoes = Cotacao.objects.all()
    return render(request,'cotacoes.html',{'cotacoes': cotacoes})

def listar_acoes(request):
    acoes = Acao.objects.all()
    return render(request, 'acoes.html', {'acoes' : acoes})


def nova_empresa(request):
    form = FormularioEmpresa(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_empresas')

    return  render(request, 'formulario_empresas.html', {'form' : form})

def atualizar_empresa(request, id):
    empresa = get_object_or_404(Empresas, pk=id)
    form = FormularioEmpresa(request.POST or None, instance = empresa)

    if form.is_valid():
        form.save()
        return redirect('lista_empresas')

    return render(request,'formulario_empresas.html', {'form' : form})

def cadastrar_acao(request,id):
    form = FormularioAcao(request.POST or None)
    empresa = Empresas.objects.all()
    empresa = Empresas.objects.filter(id = id)

    if form.is_valid():
        acao =form.save(commit= False)
        acao.empresa = (empresa[0])
        acao.save()
        return redirect('lista_empresas')

    return render(request,'formulario_acao.html', {'form' : form})

def cadastrar_cotacao(request,id):
    form = FormularioCotacao(request.POST or None)
    acao = Acao.objects.all()
    acao = Acao.objects.filter(id = id)

    if form.is_valid():
        cotacao =form.save(commit= False)
        cotacao.acao = (acao[0])
        cotacao.save()
        return redirect('listar_acoes')

    return render(request,'formulario_acao.html', {'form' : form})

