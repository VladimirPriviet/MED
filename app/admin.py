from django.contrib import admin
from .models import Paciente, Sintoma, Diagnostico

admin.site.register(Paciente)
admin.site.register(Sintoma)
admin.site.register(Diagnostico)
