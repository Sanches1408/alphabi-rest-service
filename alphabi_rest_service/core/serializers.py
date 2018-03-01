from core.models import Data
from rest_framework.serializers import ModelSerializer


class DataSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = ('title', 'measure', 'value')


class GeneralSerializer(ModelSerializer):
    class Meta:
        model = None
        fields = '__all__'
