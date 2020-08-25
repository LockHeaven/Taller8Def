import django_filters
from django_filters import CharFilter
from .models import *

class Personafilter(django_filters.FilterSet):

    class Meta:
        model = Persona
        fields = [
            'nombres',
            'apellidos',
            'tipodocumento',
            'documento',
            'fechanacimiento',
            'residencia',

        ] 