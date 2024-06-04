from rest_framework import serializers
from .models import balconista
class balconistaSerializer(serializers.ModelSerializer):

    class balconista:

        model = balconista

fields = [
'id',
'nomebalconista',
]