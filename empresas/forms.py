from django.forms import ModelForm
from .models import Empresas, Acao, Cotacao


class FormularioEmpresa(ModelForm):
    class Meta:
        model = Empresas
        fields = ['nome']

class FormularioAcao(ModelForm):
    class Meta:
        model = Acao
        fields = ['sigla']

class FormularioCotacao(ModelForm):
    class Meta:
        model = Cotacao
        fields = ['valor']