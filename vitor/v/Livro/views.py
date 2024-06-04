from rest_framework import generics
from .models import Livro
from .serializers import LivroSerializer

class LivroView(viewsets.ModelViewSet):

    queryset = Livro.objects.all()
    serializer_class = LivroSerializer