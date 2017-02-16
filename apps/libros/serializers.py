from rest_framework.serializers import ModelSerializer
from .models import Linea


class LineaSerializer(ModelSerializer):
    class Meta:
        #estado = EstadoSerializer(many=False, read_only=False)
        model = Linea
        fields = ('id', 'cod_linea','linea','presidente',
                  'telefono','direccion','estado','municipio','parroquia')
