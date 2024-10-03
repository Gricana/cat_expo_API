from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользовательское разрешение, позволяющее редактировать объект
    только его владельцу. Остальные пользователи имеют доступ только для чтения.
    """

    def has_object_permission(self, request, view, obj) -> bool:
        """
        Проверяет права на доступ к объекту.
        Доступ для чтения предоставляется всем пользователям.
        Изменять объект может только владелец.

        :param request: Запрос пользователя.
        :param view: Представление (View), к которому запрашивается доступ.
        :param obj: Объект, к которому запрашивается доступ.
        :return: True, если доступ разрешён, иначе PermissionDenied.
        """
        if request.method in permissions.SAFE_METHODS or obj.owner == request.user:
            return True

        raise PermissionDenied({
            "detail": "Отстаньте от чужого кота )"
        })
