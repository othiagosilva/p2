from rest_framework import serializers
from treinador.models import *

class RendaSerializer(serializers.ModelSerializer):
 
    class MetaRenda:
        model = Renda
        fields = (
                  'nome_renda',
                  'valor_renda',
                  )