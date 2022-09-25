from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    message = "You are not superuser"

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser


class IsSupplier(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_supplier and request.user.is_authenticated)


class IsOwnerCustomer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_customer and request.user.is_authenticated)

    message = "You must be the owner of this address"

    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user.customeruser) or request.user.is_superuser