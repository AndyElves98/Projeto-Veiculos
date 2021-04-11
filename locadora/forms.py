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