from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.contrib.auth.models import User
from .models import Paciente, Region, Comuna, Sucursal, Especialidad, Pago, Persona, Medico, Agenda
from .serializers import UserSerializer, PacienteSerializer, RegionSerializer, ComunaSerializer, SucursalSerializer, EspecialidadSerializer, PagoSerializer, PersonaSerializer, MedicoSerializer, AgendaSerializer

# Create your views here.
class ListUser(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = User.objects.get(id=id)
        serializer = UserSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def get(self, request, id=None):
        if id:
            item = User.objects.get(id=id)
            serializer = UserSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        items = User.objects.all()
        serializer = UserSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        item = get_object_or_404(User, id=id)
        item.delete()
        return Response({"status": "success", "data": "User Deleted"})

class ListPaciente(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def post(self, request):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = Paciente.objects.get(correo=id)
        serializer = PacienteSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def get(self, request, id=None):
        if id:
            item = Paciente.objects.get(correo=id)
            serializer = PacienteSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        items = Paciente.objects.all()
        serializer = PacienteSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        item = get_object_or_404(Paciente, correo=id)
        item.delete()
        return Response({"status": "success", "data": "User Deleted"})

class ListRegion(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def post(self, request):
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = Region.objects.get(id_region=id)
        serializer = RegionSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def get(self, request, id=None):
        if id:
            item = Region.objects.get(id_region=id)
            serializer = RegionSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        items = Region.objects.all()
        serializer = RegionSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        item = get_object_or_404(Region, id_region=id)
        item.delete()
        return Response({"status": "success", "data": "User Deleted"})

class ListComuna(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def post(self, request):
        serializer = ComunaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = Comuna.objects.get(id_comuna=id)
        serializer = ComunaSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def get(self, request, id=None):
        if id:
            item = Comuna.objects.get(id_comuna=id)
            serializer = ComunaSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        items = Comuna.objects.all()
        serializer = ComunaSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        item = get_object_or_404(Comuna, id_comuna=id)
        item.delete()
        return Response({"status": "success", "data": "User Deleted"})

class ListSucursal(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def post(self, request):
        serializer = SucursalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = Sucursal.objects.get(id_sucursal=id)
        serializer = SucursalSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def get(self, request, id=None):
        if id:
            item = Sucursal.objects.get(id_sucursal=id)
            serializer = SucursalSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        items = Sucursal.objects.all()
        serializer = SucursalSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        item = get_object_or_404(Sucursal, id_sucursal=id)
        item.delete()
        return Response({"status": "success", "data": "User Deleted"})

class ListEspecialidad(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def post(self, request):
        serializer = EspecialidadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = Especialidad.objects.get(id_especialidad=id)
        serializer = EspecialidadSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def get(self, request, id=None):
        if id:
            item = Especialidad.objects.get(id_especialidad=id)
            serializer = EspecialidadSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        items = Especialidad.objects.all()
        serializer = EspecialidadSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        item = get_object_or_404(Especialidad, id_especialidad=id)
        item.delete()
        return Response({"status": "success", "data": "User Deleted"})

class ListPago(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def post(self, request):
        serializer = PagoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = Pago.objects.get(id_pago=id)
        serializer = PagoSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def get(self, request, id=None):
        if id:
            item = Pago.objects.get(id_pago=id)
            serializer = PagoSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        items = Pago.objects.all()
        serializer = PagoSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        item = get_object_or_404(Pago, id_pago=id)
        item.delete()
        return Response({"status": "success", "data": "User Deleted"})

class ListPersona(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def post(self, request):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = Persona.objects.get(id_persona=id)
        serializer = PersonaSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def get(self, request, id=None):
        if id:
            item = Persona.objects.get(id_persona=id)
            serializer = PersonaSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        items = Persona.objects.all()
        serializer = PersonaSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        item = get_object_or_404(Persona, id_persona=id)
        item.delete()
        return Response({"status": "success", "data": "User Deleted"})

class ListMedico(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def post(self, request):
        serializer = MedicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = Medico.objects.get(id_medico=id)
        serializer = MedicoSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def get(self, request, id=None):
        if id:
            item = Medico.objects.get(id_medico=id)
            serializer = MedicoSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        items = Medico.objects.all()
        serializer = MedicoSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        item = get_object_or_404(Medico, id_medico=id)
        item.delete()
        return Response({"status": "success", "data": "User Deleted"})

class ListAgenda(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def post(self, request):
        serializer = AgendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = Agenda.objects.get(id_agenda=id)
        serializer = AgendaSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def get(self, request, id=None):
        if id:
            item = Agenda.objects.get(id_agenda=id)
            serializer = AgendaSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        items = Agenda.objects.all()
        serializer = AgendaSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        item = get_object_or_404(Agenda, id_agenda=id)
        item.delete()
        return Response({"status": "success", "data": "User Deleted"})