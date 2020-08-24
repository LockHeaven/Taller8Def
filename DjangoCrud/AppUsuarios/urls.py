from django.urls import path, re_path
from .views import *
urlpatterns = [
    path('',home,name = 'home'),
    path('listar/',listar,name = 'listar'),
    path('crear/',crear,name = 'crear'),
    re_path(r'^editar/(?P<id>\d+)/$',editar, name = 'editar'),
    re_path(r'^eliminar/(?P<id>\d+)/$',eliminar, name = 'eliminar'),
]