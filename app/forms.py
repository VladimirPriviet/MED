# app/forms.py
from django import forms
from .models import Paciente, Diagnostico, Sintoma, Doenca
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'nome',
            'cpf',
            'data_nascimento',
            'email',
            'telefone',
            'endereco',
            Submit('submit', 'Salvar Paciente', css_class='btn btn-success mt-2')
        )

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = '__all__'
        widgets = {
            'data_diagnostico': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'paciente',
            'doenca',
            'data_diagnostico',
            'observacoes',
            'arquivo_diagnostico',
            Submit('submit', 'Salvar Diagnóstico', css_class='btn btn-success mt-2')
        )

class SintomaForm(forms.ModelForm):
    class Meta:
        model = Sintoma
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'nome',
            'descricao',
            Submit('submit', 'Salvar Sintoma', css_class='btn btn-success mt-2')
        )

class DoencaForm(forms.ModelForm):
    class Meta:
        model = Doenca
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'nome',
            'descricao',
            'sintomas_comuns',
            Submit('submit', 'Salvar Doença', css_class='btn btn-success mt-2')
        )