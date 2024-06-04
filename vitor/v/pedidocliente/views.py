from rest_framework import generics
from .models import pedidocliente
from .serializers import pedidoclienteSerializer

class pedidoclienteView(viewsets.ModelViewSet):

    queryset = pedidocliente.objects.all()
    serializer_class = pedidoclienteSerializer