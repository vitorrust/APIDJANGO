from rest_framework import serializers
from .models import cliente
class clienteSerializer(serializers.ModelSerializer):

    class cliente:

        model = cliente

fields = [
'id',
'nomeCliente',
]