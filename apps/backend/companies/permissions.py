from rest_framework.permissions import BasePermission
from accounts.models import User


class IsSuperAdmin(BasePermission):
    """
    Autorise uniquement les SUPER_ADMIN.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.SUPER_ADMIN
        )