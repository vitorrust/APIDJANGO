from rest_framework import generics
from .models import pedido
from .serializers import pedidoSerializer

class pedidoView(viewsets.ModelViewSet):

    queryset = pedido.objects.all()
    serializer_class = pedidoSerializer