from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользователь может редактировать или удалять только свои комментарии.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешение на чтение всегда разрешено, 
        # поэтому мы разрешаем GET, HEAD или OPTIONS запросы.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешение на запись зависит от того, является ли пользователь владельцем комментария.
        return obj.author == request.user