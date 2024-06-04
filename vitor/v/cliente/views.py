from rest_framework import generics
from .models import cliente
from .serializers import clienteSerializer

class clienteView(viewsets.ModelViewSet):

    queryset = cliente.objects.all()
    serializer_class = clienteSerializer