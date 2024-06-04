from rest_framework import serializers
from .models import pedido
class pedidoSerializer(serializers.ModelSerializer):

    class pedido:

        model = pedido

fields = [
'id',
'nomepedido',
]