from rest_framework.serializers import CharField, ModelSerializer

from core.models import Compra


class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'


class CompraSerializer(ModelSerializer):  # ruff: ignore[redefined-while-unused]
    usuario = CharField(source='usuario.email', read_only=True)


class CompraSerializer(ModelSerializer):  # ruff: ignore[redefined-while-unused]
    status = CharField(source='get_status_display', read_only=True)
