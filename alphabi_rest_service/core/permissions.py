from rest_framework.permissions import BasePermission


class IsAllowedData(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('core.view_data')
