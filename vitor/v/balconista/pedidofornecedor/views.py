from rest_framework import generics
from .models import pedidofornecedor
from .serializers import pedidofornecedorSerializer

class pedidofornecedorView(viewsets.ModelViewSet):

    queryset = pedidofornecedor.objects.all()
    serializer_class = pedidofornecedorSerializer