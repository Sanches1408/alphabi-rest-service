from django.contrib.auth.models import User, Group
from core.serializers import DataSerializer
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    )
from core.permissions import IsAllowedData
from core.models import Data


class DataCreateAPIView(CreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class DataListAPIView(ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [IsAllowedData]


class DataDetailAPIView(RetrieveAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [IsAllowedData]


class DataUpdateAPIView(UpdateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class DataDeleteAPIView(DestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
