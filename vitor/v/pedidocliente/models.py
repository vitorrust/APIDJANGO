from rest_framework import serializers
from .models import pedidoclientecliente
class pedidoclienteclienteSerializer(serializers.ModelSerializer):

    class pedidocliente:

        model = pedidocliente

fields = [
'id',
'nomepedidocliente',
]