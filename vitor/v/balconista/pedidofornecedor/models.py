from rest_framework import serializers
from .models import pedidofornecedorcliente
class pedidofornecedorclienteSerializer(serializers.ModelSerializer):

    class pedidofornecedor:

        model = pedidofornecedor

fields = [
'id',
'nomepedidofornecedor',
]