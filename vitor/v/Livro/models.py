from rest_framework import serializers
from .models import Livro
class LivroSerializer(serializers.ModelSerializer):

    class Livro:

        model = Livro

fields = [
'id',
'nomeLivro',
]