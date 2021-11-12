from django.urls import path
from django.conf.urls import include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('pacientes/', views.ListPaciente.as_view(), name="pacientes"),
    path('pacientes/<id>', views.ListPaciente.as_view(), name="pacientes"),
    path('users/', views.ListUser.as_view(), name="users"),
    path('users/<id>', views.ListUser.as_view(), name="users"),
    path('agenda/', views.ListAgenda.as_view(), name="agenda"),
    path('agenda/<id>', views.ListAgenda.as_view(), name="agenda"),
    path('trabajadores/', views.ListTrabajador.as_view(), name="trabajadores"),
    path('trabajadores/<id>', views.ListTrabajador.as_view(), name="trabajadores"),
    path('cargos/', views.ListCargo.as_view(), name="cargos"),
    path('cargos/<id>', views.ListCargo.as_view(), name="cargos"),
    path('pagos/', views.ListPago.as_view(), name="pagos"),
    path('pagos/<id>', views.ListPago.as_view(), name="pagos"),
    path('especialidades/', views.ListEspecialidad.as_view(), name="especialidades"),
    path('especialidades/<id>', views.ListEspecialidad.as_view(), name="especialidades"),
    path('sucursales/', views.ListSucursal.as_view(), name="sucursales"),
    path('sucursales/<id>', views.ListSucursal.as_view(), name="sucursales"),
    path('comunas/', views.ListComuna.as_view(), name="comunas"),
    path('comunas/<id>', views.ListComuna.as_view(), name="comunas"),
    path('regiones/', views.ListRegion.as_view(), name="regiones"),
    path('regiones/<id>', views.ListRegion.as_view(), name="regiones"),
    path('token-auth/', obtain_auth_token, name='token_auth'),
]