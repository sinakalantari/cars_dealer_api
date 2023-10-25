from rest_framework.permissions import BasePermission
from cars_account.models import UserProfileModel, Role


class IsSupervisor(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            permission = Role.objects.filter(userprofilemodel=request.user.userprofilemodel).values_list('id')
            print(permission)
            return bool(request.user and request.user.is_authenticated and (3,) in permission)

        return bool(request.user and request.user.is_authenticated)


class IsManagement(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            permission = Role.objects.filter(userprofilemodel=request.user.userprofilemodel).values_list('id')
            return bool(request.user and request.user.is_authenticated and (2,) in permission)

        return bool(request.user and request.user.is_authenticated)


class IsSystemAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            permission = Role.objects.filter(userprofilemodel=request.user.userprofilemodel).values_list('id')
            return bool(request.user and request.user.is_authenticated and (1,) in permission)

        return bool(request.user and request.user.is_authenticated)


class IsClient(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            permission = Role.objects.filter(userprofilemodel=request.user.userprofilemodel).values_list('id')
            return bool(request.user and request.user.is_authenticated and (4,) in permission)

        return bool(request.user and request.user.is_authenticated)


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
