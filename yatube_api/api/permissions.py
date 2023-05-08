from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly


class OnlyAuthorCanModify(IsAuthenticatedOrReadOnly):
    """Only author can modify. Others read only."""
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.author == request.user
