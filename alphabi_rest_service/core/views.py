from core.serializers import GeneralSerializer
from core.permissions import GeneralPermission
from rest_framework.viewsets import ModelViewSet
from django.apps import apps
from django.contrib.contenttypes.models import ContentType


class GeneralViewSet(ModelViewSet):
    permission_classes = [GeneralPermission]

    def dispatch(self, request, *args, **kwargs):
        self.model = self.get_model()
        return super(GeneralViewSet, self).dispatch(request, *args, **kwargs)

    def get_model(self):
        model_name = self.kwargs.get('model')
        return apps.get_model(ContentType.objects.get(model=model_name).app_label,
                              model_name)

    def get_queryset(self):
        return self.model.objects.all()
    
    def get_serializer_class(self):
        GeneralSerializer.Meta.model = self.model
        return GeneralSerializer
