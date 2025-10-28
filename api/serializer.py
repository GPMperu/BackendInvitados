from rest_framework import serializers
from .models import Invitado

class InvitadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitado
        fields = '__all__'

class InvitadoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitado
        fields = ['socio', 'fecha_evento', 'ubicacion']
        