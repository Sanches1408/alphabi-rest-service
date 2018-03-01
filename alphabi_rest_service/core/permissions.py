from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class GeneralPermission(BasePermission):
    def has_permission(self, request, view):
        content_type = ContentType.objects.get_for_model(view.model)
        all_permissions = Permission.objects.filter(content_type=content_type)
        for permission in all_permissions:
            if request.user.has_perm("core." + permission.codename):
                return True
        return False
