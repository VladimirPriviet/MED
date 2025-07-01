# app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages # Importe messages se for usar
from .models import Paciente, Sintoma, Doenca, Diagnostico # Certifique-se de que todas as models necessárias estão importadas
from .forms import PacienteForm, DiagnosticoForm, SintomaForm, DoencaForm # Importe todos os formulários se for usar

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class PacientesListView(View): # Nome alterado para clareza e consistência com a lista
    def get(self, request, *args, **kwargs):
        pacientes = Paciente.objects.all()
        return render(request, 'pacientes.html', {'pacientes': pacientes})

class DiagnosticosListView(View): # Nome alterado para clareza e consistência com a lista
    def get(self, request, *args, **kwargs):
        diagnosticos = Diagnostico.objects.all() # Alterado para all() para simplificar o exemplo, select_related pode ser adicionado depois
        return render(request, 'diagnosticos.html', {'diagnosticos': diagnosticos})

# ... (adicione as outras views que eu forneci anteriormente, como PacienteDetailView, PacienteCreateView, etc.)
# ... (adicione as views para Sintomas e Doenças, se necessário)