"""formularios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from empresas.views import listar_empresas, cadastrar_acao, cadastrar_cotacao, listar_acoes, listar_cotacoes
from empresas.views import nova_empresa
from empresas.views import atualizar_empresa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_empresas, name = "lista_empresas"),
    path('adicionar', nova_empresa, name = "adicionar_empresa"),
    path('atualizar/<int:id>/', atualizar_empresa, name = "atualizar_empresa"),
    path('add_acao/<int:id>/', cadastrar_acao, name="adicionar_acao"),
    path('add_cotacao/<int:id>',cadastrar_cotacao, name="adicionar_cotacao"),
    path('lista_acoes',listar_acoes,name="listar_acoes"),
    path('lsita_cotacao',listar_cotacoes,name="listar_cotacoes")
]
