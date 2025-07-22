from django.contrib import admin
from django.urls import path
from app import views  # <-- esta linha é essencial!
from app.views import ConsultasListView  # ✅ CORRETO


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('pacientes/', views.PacientesListView.as_view(), name='pacientes_list'),
    path('diagnosticos/', views.DiagnosticosListView.as_view(), name='diagnosticos_list'),
    path('doencas/', views.doencas_view, name='doencas'),
    path('consultas/', ConsultasListView.as_view(), name='consultas'),
    path('casos-mais-registrados/', views.CasosMaisRegistradosView.as_view(), name='casos_mais_registrados'),
    
]
