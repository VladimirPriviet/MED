
from django.contrib import admin
from .models import Paciente, Sintoma, Doenca, Diagnostico, Consulta 


admin.site.site_header = "Painel Administrativo - MED+"
admin.site.site_title = "Administração MED+"
admin.site.index_title = "Bem-vindo ao painel de gestão do sistema MED+"


admin.site.register(Paciente)
admin.site.register(Sintoma)
admin.site.register(Doenca) 
admin.site.register(Diagnostico)
admin.site.register(Consulta) 

