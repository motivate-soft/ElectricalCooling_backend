from rest_framework import mixins, generics, permissions, authentication
from rest_framework.permissions import BasePermission

from cooling.models import Cooling
from cooling.serializers import CoolingSerializer


class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class AdminAuthenticationPermission(permissions.BasePermission):
    ADMIN_ONLY_AUTH_CLASSES = [authentication.BasicAuthentication,
                               authentication.SessionAuthentication]

    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated():
            return user.is_superuser or not any(
                isinstance(request._authenticator, x) for x in self.ADMIN_ONLY_AUTH_CLASSES)
        return False


class CoolingListView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    """
    List View

    """
    permission_classes = (IsAdminUser,)
    queryset = Cooling.objects.all()
    serializer_class = CoolingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request.data['owner'] = request.user.id
        return self.create(request, *args, **kwargs)


class MyCoolingListView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    """
    List View

    """
    queryset = Cooling.objects.filter()
    serializer_class = CoolingSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Cooling.objects.filter(owner=user)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request.data['owner'] = request.user.id
        return self.create(request, *args, **kwargs)


class CoolingDetailView(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    """
    Detail View

    """

    queryset = Cooling.objects.all()
    serializer_class = CoolingSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# API endpoints
# class CoolingListView(mixins.ListModelMixin,
#                       mixins.CreateModelMixin,
#                       generics.GenericAPIView):
#     """
#     List View
#
#     """
#     queryset = Cooling.objects.all()
#     serializer_class = CoolingSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class CoolingDetailView(mixins.RetrieveModelMixin,
#                         mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin,
#                         generics.GenericAPIView):
#     """
#     Detail View
#
#     """
#
#     queryset = Cooling.objects.all()
#     serializer_class = CoolingSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
