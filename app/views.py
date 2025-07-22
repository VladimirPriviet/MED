from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.db.models import Count
from .models import Paciente, Sintoma, Doenca, Diagnostico, Consulta
from .forms import PacienteForm, DiagnosticoForm, SintomaForm, DoencaForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class PacientesListView(View):
    def get(self, request, *args, **kwargs):
        pacientes = Paciente.objects.all()
        return render(request, 'pacientes.html', {'pacientes': pacientes})


class DiagnosticosListView(View): 
    def get(self, request, *args, **kwargs):
        diagnosticos = Diagnostico.objects.all() 
        return render(request, 'diagnosticos.html', {'diagnosticos': diagnosticos})


def doencas_view(request):
    doencas = Doenca.objects.all()  
    return render(request, 'doencas.html', {'doencas': doencas})


class ConsultasListView(View):
    def get(self, request, *args, **kwargs):
        consultas = Consulta.objects.all()
        return render(request, 'consultas.html', {'consultas': consultas})


class CasosMaisRegistradosView(View):
    def get(self, request, *args, **kwargs):
        casos = Doenca.objects.annotate(
            quantidade=Count('diagnostico')
        ).order_by('-quantidade')[:3]
        return render(request, 'casosemalta.html', {'casos': casos})


