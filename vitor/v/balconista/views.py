from rest_framework import generics
from .models import balconista
from .serializers import balconistaSerializer

class balconistaView(viewsets.ModelViewSet):

    queryset = balconista.objects.all()
    serializer_class = balconistaSerializer