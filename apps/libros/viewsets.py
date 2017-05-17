from rest_framework import viewsets
from .serializers import LineaSerializer
from .models import Linea


class LineaViewSet(viewsets.ModelViewSet):
    serializer_class = LineaSerializer
    queryset = Linea.objects.all()
