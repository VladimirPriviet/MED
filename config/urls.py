# config/urls.py
from django.contrib import admin
from django.urls import path
# Importe as views com os nomes corretos (ListView)
from app.views import IndexView, PacientesListView, DiagnosticosListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    # Use as views com os nomes corretos (ListView)
    path('pacientes/', PacientesListView.as_view(), name='pacientes_list'), # Nome da URL para consistência
    path('diagnosticos/', DiagnosticosListView.as_view(), name='diagnosticos_list'), # Nome da URL para consistência
    
]