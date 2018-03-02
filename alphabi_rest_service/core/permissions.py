from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class GeneralPermission(BasePermission):
    def has_permission(self, request, view):
        if view.get_user_permissions():
            return True
        else:
            return False
