from rest_framework import serializers
from .models import fornecedor
class fornecedorSerializer(serializers.ModelSerializer):

    class fornecedor:

        model = fornecedor

fields = [
'id',
'nomefornecedor',
]