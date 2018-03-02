from core.serializers import GeneralSerializer
from core.permissions import GeneralPermission
from rest_framework.viewsets import ModelViewSet
from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


class GeneralViewSet(ModelViewSet):
    permission_classes = [GeneralPermission]

    def dispatch(self, request, *args, **kwargs):
        self.model = self.get_model()
        return super(GeneralViewSet, self).dispatch(request, *args, **kwargs)

    def get_model(self):
        model_name = self.kwargs.get('model').lower()
        return apps.get_model(ContentType.objects.get(model=model_name).app_label,
                              model_name)

    def get_queryset(self):
        return self.model.objects.all()
    
    def get_user_permissions(self):
        content_type = ContentType.objects.get_for_model(self.model)
        all_permissions = Permission.objects.filter(content_type=content_type)
        permissions = []
        for p in all_permissions:
            if self.request.user.has_perm("core." + p.codename):
                permissions.append(p.codename)
        return permissions

    def get_serializer_class(self):
        GeneralSerializer.Meta.model = self.model
        permissions = self.get_user_permissions()
        model_fields = [f.name for f in self.model._meta.get_fields()]
        fields = []
        for p in permissions:
            if p in model_fields:
                fields.append(p)
        GeneralSerializer.Meta.fields = fields
        return GeneralSerializer
