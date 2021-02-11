from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from cooling.models import Cooling
from cooling.serializers import CoolingSerializer


# API endpoints
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'cooling': reverse('cooling-list', request=request, format=format)
    })


class CoolingListView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    """
    List View

    """
    queryset = Cooling.objects.all()
    serializer_class = CoolingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
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
