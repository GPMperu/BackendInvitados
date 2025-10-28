from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import InvitadoSerializer, InvitadoSimpleSerializer
from .models import Invitado
from django.db.models import Q

# Create your views here.
class InvitadoViewSet(viewsets.ModelViewSet):
    serializer_class = InvitadoSerializer
    queryset = Invitado.objects.all()

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(
                {"message": "Invitado eliminado correctamente"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"detail": f"Error al eliminar el invitado: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=['get'])
    def simple(self, request):
        """Endpoint que solo devuelve socio, fecha_evento y ubicacion"""
        invitados = Invitado.objects.all()
        serializer = InvitadoSimpleSerializer(invitados, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def buscar(self, request):
        """
        Busca invitados usando socio, fecha_evento y/o ubicacion como filtros,
        devuelve todos los campos del invitado.
        """
        socio = request.query_params.get('socio', None)
        fecha_evento = request.query_params.get('fecha_evento', None)
        ubicacion = request.query_params.get('ubicacion', None)

        # Construir el filtro
        filtros = Q()
        if socio:
            filtros &= Q(socio__icontains=socio)
        if fecha_evento:
            filtros &= Q(fecha_evento=fecha_evento)
        if ubicacion:
            filtros &= Q(ubicacion__icontains=ubicacion)

        # Si no hay filtros, devolver mensaje de error
        if not (socio or fecha_evento or ubicacion):
            return Response(
                {"message": "Proporciona al menos un parámetro de búsqueda: socio, fecha_evento o ubicacion"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Realizar la búsqueda
        invitados = Invitado.objects.filter(filtros)
        serializer = InvitadoSerializer(invitados, many=True)
        return Response(serializer.data)