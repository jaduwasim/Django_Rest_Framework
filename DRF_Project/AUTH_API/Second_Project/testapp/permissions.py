from rest_framework.permissions import BasePermission, SAFE_METHODS

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        name = request.user.username
        if name.lower()=='sunny':
            return True
        elif name != '' and len(name)%2 == 0 and request.method in SAFE_METHODS:
            return True
        return False