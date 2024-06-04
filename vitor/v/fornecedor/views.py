from rest_framework import generics
from .models import fornecedor
from .serializers import fornecedorSerializer

class fornecedorView(viewsets.ModelViewSet):

    queryset = fornecedor.objects.all()
    serializer_class = fornecedorSerializer