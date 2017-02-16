from rest_framework.serializers import ModelSerializer
from .models import Municipio


class MunicipioSerializer(ModelSerializer):
    class Meta:
        model = Municipio
        fields = ('id', 'municipio', 'estado','cod_municipio')

    def __unicode__(self):
        return self.municipio
