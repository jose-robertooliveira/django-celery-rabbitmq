from rest_framework import serializers, viewsets
from .models import Proposta


class PropostaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proposta
        fields = '__all__'

class PropostaViewSet(viewsets.ModelViewSet):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer

