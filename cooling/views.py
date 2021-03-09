import jsonpickle
from rest_framework import mixins, generics, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.permissions import BasePermission
from rest_framework.response import Response

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


@api_view(['POST'])
def solve_thermal_model(json_input):
    print("json_input", json_input)

    component_temperatures = [
        {
            "AvgTemperature": 50.0,
            "MaxTemperature": 60.0,
            "Name": "Stator"
        },
        {
            "AvgTemperature": 40.0,
            "MaxTemperature": 45.0,
            "Name": "Housing"
        },
        {
            "AvgTemperature": 80.0,
            "MaxTemperature": 90.0,
            "Name": "Rotor"
        },
        {
            "AvgTemperature": 95,
            "MaxTemperature": 100,
            "Name": "Winding"
        },
        {
            "AvgTemperature": 66.0,
            "MaxTemperature": 77.2,
            "Name": "Magnet"
        }
    ]

    winding_temperatures = [
        [
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 72.58181832904175
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_0_1",
                "RadialLocation": 0,
                "TangentialLocation": 1,
                "Temperature": 73.70040723881536
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_0_2",
                "RadialLocation": 0,
                "TangentialLocation": 2,
                "Temperature": 74.51208748711518
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_0_3",
                "RadialLocation": 0,
                "TangentialLocation": 3,
                "Temperature": 74.91800850508933
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_0_4",
                "RadialLocation": 0,
                "TangentialLocation": 4,
                "Temperature": 74.9335982135303
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_0_5",
                "RadialLocation": 0,
                "TangentialLocation": 5,
                "Temperature": 74.5503576422238
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_0_6",
                "RadialLocation": 0,
                "TangentialLocation": 6,
                "Temperature": 73.70365499444013
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_0_7",
                "RadialLocation": 0,
                "TangentialLocation": 7,
                "Temperature": 72.21921579026937
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_0_8",
                "RadialLocation": 0,
                "TangentialLocation": 8,
                "Temperature": 69.55373317860102
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 74.41147901503595
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_1_1",
                "RadialLocation": 1,
                "TangentialLocation": 1,
                "Temperature": 75.9480385932908
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_1_2",
                "RadialLocation": 1,
                "TangentialLocation": 2,
                "Temperature": 77.0108640325643
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_1_3",
                "RadialLocation": 1,
                "TangentialLocation": 3,
                "Temperature": 77.53963588547136
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_1_4",
                "RadialLocation": 1,
                "TangentialLocation": 4,
                "Temperature": 77.55873374254968
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_1_5",
                "RadialLocation": 1,
                "TangentialLocation": 5,
                "Temperature": 77.05910123860193
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_1_6",
                "RadialLocation": 1,
                "TangentialLocation": 6,
                "Temperature": 75.9670503091751
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_1_7",
                "RadialLocation": 1,
                "TangentialLocation": 7,
                "Temperature": 74.09119751760252
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_1_8",
                "RadialLocation": 1,
                "TangentialLocation": 8,
                "Temperature": 70.86804212456799
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 75.67644876925002
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_2_1",
                "RadialLocation": 2,
                "TangentialLocation": 1,
                "Temperature": 77.53005140915606
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_2_2",
                "RadialLocation": 2,
                "TangentialLocation": 2,
                "Temperature": 78.78418739523666
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_2_3",
                "RadialLocation": 2,
                "TangentialLocation": 3,
                "Temperature": 79.40755993502589
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_2_4",
                "RadialLocation": 2,
                "TangentialLocation": 4,
                "Temperature": 79.43281846709407
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_2_5",
                "RadialLocation": 2,
                "TangentialLocation": 5,
                "Temperature": 78.8532786499413
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_2_6",
                "RadialLocation": 2,
                "TangentialLocation": 6,
                "Temperature": 77.59485865645813
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_2_7",
                "RadialLocation": 2,
                "TangentialLocation": 7,
                "Temperature": 75.46490869423602
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_2_8",
                "RadialLocation": 2,
                "TangentialLocation": 8,
                "Temperature": 71.89220973764975
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 76.54644945607524
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_3_1",
                "RadialLocation": 3,
                "TangentialLocation": 1,
                "Temperature": 78.6337145616754
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_3_2",
                "RadialLocation": 3,
                "TangentialLocation": 2,
                "Temperature": 80.03399659270583
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_3_3",
                "RadialLocation": 3,
                "TangentialLocation": 3,
                "Temperature": 80.73192414337551
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_3_4",
                "RadialLocation": 3,
                "TangentialLocation": 4,
                "Temperature": 80.76526581619413
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_3_5",
                "RadialLocation": 3,
                "TangentialLocation": 5,
                "Temperature": 80.1299692317749
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_3_6",
                "RadialLocation": 3,
                "TangentialLocation": 6,
                "Temperature": 78.75386625436111
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_3_7",
                "RadialLocation": 3,
                "TangentialLocation": 7,
                "Temperature": 76.44581066180137
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_3_8",
                "RadialLocation": 3,
                "TangentialLocation": 8,
                "Temperature": 72.62780785938966
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 77.14886880777348
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_4_1",
                "RadialLocation": 4,
                "TangentialLocation": 1,
                "Temperature": 79.40548056508466
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_4_2",
                "RadialLocation": 4,
                "TangentialLocation": 2,
                "Temperature": 80.91515548880034
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_4_3",
                "RadialLocation": 4,
                "TangentialLocation": 3,
                "Temperature": 81.67069949539135
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_4_4",
                "RadialLocation": 4,
                "TangentialLocation": 4,
                "Temperature": 81.71244116710383
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_4_5",
                "RadialLocation": 4,
                "TangentialLocation": 5,
                "Temperature": 81.03826220564366
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_4_6",
                "RadialLocation": 4,
                "TangentialLocation": 6,
                "Temperature": 79.57804933537545
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_4_7",
                "RadialLocation": 4,
                "TangentialLocation": 7,
                "Temperature": 77.14241709836621
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_4_8",
                "RadialLocation": 4,
                "TangentialLocation": 8,
                "Temperature": 73.14860616716804
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 77.56678312366334
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_5_1",
                "RadialLocation": 5,
                "TangentialLocation": 1,
                "Temperature": 79.94453160738519
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_5_2",
                "RadialLocation": 5,
                "TangentialLocation": 2,
                "Temperature": 81.53437856444589
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_5_3",
                "RadialLocation": 5,
                "TangentialLocation": 3,
                "Temperature": 82.33327530832985
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_5_4",
                "RadialLocation": 5,
                "TangentialLocation": 4,
                "Temperature": 82.38259849634174
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_5_5",
                "RadialLocation": 5,
                "TangentialLocation": 5,
                "Temperature": 81.681425238577
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_5_6",
                "RadialLocation": 5,
                "TangentialLocation": 6,
                "Temperature": 80.1612776156787
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_5_7",
                "RadialLocation": 5,
                "TangentialLocation": 7,
                "Temperature": 77.63431282815162
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_5_8",
                "RadialLocation": 5,
                "TangentialLocation": 8,
                "Temperature": 73.5148550419122
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 77.85323204443148
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_6_1",
                "RadialLocation": 6,
                "TangentialLocation": 1,
                "Temperature": 80.3157519895346
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_6_2",
                "RadialLocation": 6,
                "TangentialLocation": 2,
                "Temperature": 81.96266922693884
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_6_3",
                "RadialLocation": 6,
                "TangentialLocation": 3,
                "Temperature": 82.79303615494314
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_6_4",
                "RadialLocation": 6,
                "TangentialLocation": 4,
                "Temperature": 82.84852644547017
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_6_5",
                "RadialLocation": 6,
                "TangentialLocation": 5,
                "Temperature": 82.12888758140289
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_6_6",
                "RadialLocation": 6,
                "TangentialLocation": 6,
                "Temperature": 80.56681081985906
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_6_7",
                "RadialLocation": 6,
                "TangentialLocation": 7,
                "Temperature": 77.97567944569988
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_6_8",
                "RadialLocation": 6,
                "TangentialLocation": 8,
                "Temperature": 73.76815219849672
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 78.04169347016101
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_7_1",
                "RadialLocation": 7,
                "TangentialLocation": 1,
                "Temperature": 80.56076153512889
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_7_2",
                "RadialLocation": 7,
                "TangentialLocation": 2,
                "Temperature": 82.24617829070863
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_7_3",
                "RadialLocation": 7,
                "TangentialLocation": 3,
                "Temperature": 83.0980512001992
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_7_4",
                "RadialLocation": 7,
                "TangentialLocation": 4,
                "Temperature": 83.1580454816017
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_7_5",
                "RadialLocation": 7,
                "TangentialLocation": 5,
                "Temperature": 82.42626365150035
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_7_6",
                "RadialLocation": 7,
                "TangentialLocation": 6,
                "Temperature": 80.83617927245761
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_7_7",
                "RadialLocation": 7,
                "TangentialLocation": 7,
                "Temperature": 78.20207295961518
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_7_8",
                "RadialLocation": 7,
                "TangentialLocation": 8,
                "Temperature": 73.93570323727427
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 78.15267535611696
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_8_1",
                "RadialLocation": 8,
                "TangentialLocation": 1,
                "Temperature": 80.70533177276623
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_8_2",
                "RadialLocation": 8,
                "TangentialLocation": 2,
                "Temperature": 82.41375605291357
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_8_3",
                "RadialLocation": 8,
                "TangentialLocation": 3,
                "Temperature": 83.27855250354888
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_8_4",
                "RadialLocation": 8,
                "TangentialLocation": 4,
                "Temperature": 83.34130709851343
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_8_5",
                "RadialLocation": 8,
                "TangentialLocation": 5,
                "Temperature": 82.60230783777483
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_8_6",
                "RadialLocation": 8,
                "TangentialLocation": 6,
                "Temperature": 80.995510994599
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_8_7",
                "RadialLocation": 8,
                "TangentialLocation": 7,
                "Temperature": 78.33578364868791
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_8_8",
                "RadialLocation": 8,
                "TangentialLocation": 8,
                "Temperature": 74.03445545493034
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 78.19759795068111
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_9_1",
                "RadialLocation": 9,
                "TangentialLocation": 1,
                "Temperature": 80.7639154149719
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_9_2",
                "RadialLocation": 9,
                "TangentialLocation": 2,
                "Temperature": 82.48168247644381
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_9_3",
                "RadialLocation": 9,
                "TangentialLocation": 3,
                "Temperature": 83.35166324261542
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_9_4",
                "RadialLocation": 9,
                "TangentialLocation": 4,
                "Temperature": 83.41540385034735
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_9_5",
                "RadialLocation": 9,
                "TangentialLocation": 5,
                "Temperature": 82.67329403310963
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_9_6",
                "RadialLocation": 9,
                "TangentialLocation": 6,
                "Temperature": 81.05954057792484
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_9_7",
                "RadialLocation": 9,
                "TangentialLocation": 7,
                "Temperature": 78.38931711103803
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_9_8",
                "RadialLocation": 9,
                "TangentialLocation": 8,
                "Temperature": 74.07385463918544
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 78.18085634918972
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_10_1",
                "RadialLocation": 10,
                "TangentialLocation": 1,
                "Temperature": 80.7421066418279
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_10_2",
                "RadialLocation": 10,
                "TangentialLocation": 2,
                "Temperature": 82.45628225119445
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_10_3",
                "RadialLocation": 10,
                "TangentialLocation": 3,
                "Temperature": 83.32403250259588
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_10_4",
                "RadialLocation": 10,
                "TangentialLocation": 4,
                "Temperature": 83.38693599711259
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_10_5",
                "RadialLocation": 10,
                "TangentialLocation": 5,
                "Temperature": 82.64544024005977
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_10_6",
                "RadialLocation": 10,
                "TangentialLocation": 6,
                "Temperature": 81.03381764063643
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_10_7",
                "RadialLocation": 10,
                "TangentialLocation": 7,
                "Temperature": 78.3673097258551
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_10_8",
                "RadialLocation": 10,
                "TangentialLocation": 8,
                "Temperature": 74.05735562125892
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 78.100568889705
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_11_1",
                "RadialLocation": 11,
                "TangentialLocation": 1,
                "Temperature": 80.6375539618755
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_11_2",
                "RadialLocation": 11,
                "TangentialLocation": 2,
                "Temperature": 82.33491427951
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_11_3",
                "RadialLocation": 11,
                "TangentialLocation": 3,
                "Temperature": 83.19284006940767
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_11_4",
                "RadialLocation": 11,
                "TangentialLocation": 4,
                "Temperature": 83.25298181186709
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_11_5",
                "RadialLocation": 11,
                "TangentialLocation": 5,
                "Temperature": 82.51580153413268
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_11_6",
                "RadialLocation": 11,
                "TangentialLocation": 6,
                "Temperature": 80.91548831907127
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_11_7",
                "RadialLocation": 11,
                "TangentialLocation": 7,
                "Temperature": 78.26717662576051
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_11_8",
                "RadialLocation": 11,
                "TangentialLocation": 8,
                "Temperature": 73.98291500633546
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 77.94819840455675
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_12_1",
                "RadialLocation": 12,
                "TangentialLocation": 1,
                "Temperature": 80.4395365025477
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_12_2",
                "RadialLocation": 12,
                "TangentialLocation": 2,
                "Temperature": 82.10555068277512
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_12_3",
                "RadialLocation": 12,
                "TangentialLocation": 3,
                "Temperature": 82.94538454320514
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_12_4",
                "RadialLocation": 12,
                "TangentialLocation": 4,
                "Temperature": 83.0006770861728
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_12_5",
                "RadialLocation": 12,
                "TangentialLocation": 5,
                "Temperature": 82.27181775516357
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_12_6",
                "RadialLocation": 12,
                "TangentialLocation": 6,
                "Temperature": 80.69280262040022
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_12_7",
                "RadialLocation": 12,
                "TangentialLocation": 7,
                "Temperature": 78.07860402958815
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_12_8",
                "RadialLocation": 12,
                "TangentialLocation": 8,
                "Temperature": 73.84254505410219
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 77.70696577761959
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_13_1",
                "RadialLocation": 13,
                "TangentialLocation": 1,
                "Temperature": 80.1271466268521
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_13_2",
                "RadialLocation": 13,
                "TangentialLocation": 2,
                "Temperature": 81.74492379018922
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_13_3",
                "RadialLocation": 13,
                "TangentialLocation": 3,
                "Temperature": 82.55725863340867
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_13_4",
                "RadialLocation": 13,
                "TangentialLocation": 4,
                "Temperature": 82.60541277462707
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_13_5",
                "RadialLocation": 13,
                "TangentialLocation": 5,
                "Temperature": 81.88950664664301
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_13_6",
                "RadialLocation": 13,
                "TangentialLocation": 6,
                "Temperature": 80.34330027242375
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_13_7",
                "RadialLocation": 13,
                "TangentialLocation": 7,
                "Temperature": 77.78179429699672
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_13_8",
                "RadialLocation": 13,
                "TangentialLocation": 8,
                "Temperature": 73.62081603810377
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 77.34875457397818
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_14_1",
                "RadialLocation": 14,
                "TangentialLocation": 1,
                "Temperature": 79.66584785984071
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_14_2",
                "RadialLocation": 14,
                "TangentialLocation": 2,
                "Temperature": 81.2151126433599
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_14_3",
                "RadialLocation": 14,
                "TangentialLocation": 3,
                "Temperature": 81.98905428039868
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_14_4",
                "RadialLocation": 14,
                "TangentialLocation": 4,
                "Temperature": 82.02761559425754
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_14_5",
                "RadialLocation": 14,
                "TangentialLocation": 5,
                "Temperature": 81.33024054549118
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_14_6",
                "RadialLocation": 14,
                "TangentialLocation": 6,
                "Temperature": 79.83054377053894
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_14_7",
                "RadialLocation": 14,
                "TangentialLocation": 7,
                "Temperature": 77.34423876441168
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_14_8",
                "RadialLocation": 14,
                "TangentialLocation": 8,
                "Temperature": 73.2920211748338
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 76.82921425937397
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_15_1",
                "RadialLocation": 15,
                "TangentialLocation": 1,
                "Temperature": 79.00240849009862
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_15_2",
                "RadialLocation": 15,
                "TangentialLocation": 2,
                "Temperature": 80.45884856333817
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_15_3",
                "RadialLocation": 15,
                "TangentialLocation": 3,
                "Temperature": 81.18203819389733
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_15_4",
                "RadialLocation": 15,
                "TangentialLocation": 4,
                "Temperature": 81.20859687921751
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_15_5",
                "RadialLocation": 15,
                "TangentialLocation": 5,
                "Temperature": 80.53653715454709
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_15_6",
                "RadialLocation": 15,
                "TangentialLocation": 6,
                "Temperature": 79.09967758172431
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_15_7",
                "RadialLocation": 15,
                "TangentialLocation": 7,
                "Temperature": 76.71605080607027
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_15_8",
                "RadialLocation": 15,
                "TangentialLocation": 8,
                "Temperature": 72.81576888486396
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 76.08209110524315
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_16_1",
                "RadialLocation": 16,
                "TangentialLocation": 1,
                "Temperature": 78.06036127402898
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_16_2",
                "RadialLocation": 16,
                "TangentialLocation": 2,
                "Temperature": 79.3964309665843
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_16_3",
                "RadialLocation": 16,
                "TangentialLocation": 3,
                "Temperature": 80.05602537886693
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_16_4",
                "RadialLocation": 16,
                "TangentialLocation": 4,
                "Temperature": 80.06876397281054
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_16_5",
                "RadialLocation": 16,
                "TangentialLocation": 5,
                "Temperature": 79.430031291331
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_16_6",
                "RadialLocation": 16,
                "TangentialLocation": 6,
                "Temperature": 78.07463802509203
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_16_7",
                "RadialLocation": 16,
                "TangentialLocation": 7,
                "Temperature": 75.82602400011766
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_16_8",
                "RadialLocation": 16,
                "TangentialLocation": 8,
                "Temperature": 72.13213350804267
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 75.02286532451355
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_17_1",
                "RadialLocation": 17,
                "TangentialLocation": 1,
                "Temperature": 76.75030450270468
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_17_2",
                "RadialLocation": 17,
                "TangentialLocation": 2,
                "Temperature": 77.94057063232222
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_17_3",
                "RadialLocation": 17,
                "TangentialLocation": 3,
                "Temperature": 78.52647382314528
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_17_4",
                "RadialLocation": 17,
                "TangentialLocation": 4,
                "Temperature": 78.5252789431181
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_17_5",
                "RadialLocation": 17,
                "TangentialLocation": 5,
                "Temperature": 77.92835222058316
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_17_6",
                "RadialLocation": 17,
                "TangentialLocation": 6,
                "Temperature": 76.67285702335232
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_17_7",
                "RadialLocation": 17,
                "TangentialLocation": 7,
                "Temperature": 74.59238168055018
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_17_8",
                "RadialLocation": 17,
                "TangentialLocation": 8,
                "Temperature": 71.16643771041984
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 73.65066256406838
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_18_1",
                "RadialLocation": 18,
                "TangentialLocation": 1,
                "Temperature": 75.10355400196494
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_18_2",
                "RadialLocation": 18,
                "TangentialLocation": 2,
                "Temperature": 76.14516689539067
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_18_3",
                "RadialLocation": 18,
                "TangentialLocation": 3,
                "Temperature": 76.65943561887816
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_18_4",
                "RadialLocation": 18,
                "TangentialLocation": 4,
                "Temperature": 76.64779966862115
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_18_5",
                "RadialLocation": 18,
                "TangentialLocation": 5,
                "Temperature": 76.09735154605815
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_18_6",
                "RadialLocation": 18,
                "TangentialLocation": 6,
                "Temperature": 74.9491348988858
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_18_7",
                "RadialLocation": 18,
                "TangentialLocation": 7,
                "Temperature": 73.05092502962128
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "RotorWinding-Leading_Core_0_18_8",
                "RadialLocation": 18,
                "TangentialLocation": 8,
                "Temperature": 69.92704900283142
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 74.54843254484513
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_0_1",
                "RadialLocation": 0,
                "TangentialLocation": 1,
                "Temperature": 75.28387489874515
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_0_2",
                "RadialLocation": 0,
                "TangentialLocation": 2,
                "Temperature": 75.91349730735445
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_0_3",
                "RadialLocation": 0,
                "TangentialLocation": 3,
                "Temperature": 76.24088906416333
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_0_4",
                "RadialLocation": 0,
                "TangentialLocation": 4,
                "Temperature": 76.24060118361616
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_0_5",
                "RadialLocation": 0,
                "TangentialLocation": 5,
                "Temperature": 75.89343862117579
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_0_6",
                "RadialLocation": 0,
                "TangentialLocation": 6,
                "Temperature": 75.14187303323882
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_0_7",
                "RadialLocation": 0,
                "TangentialLocation": 7,
                "Temperature": 73.83554240829082
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_0_8",
                "RadialLocation": 0,
                "TangentialLocation": 8,
                "Temperature": 71.51424727081094
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 76.02380831846638
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_1_1",
                "RadialLocation": 1,
                "TangentialLocation": 1,
                "Temperature": 77.14406744006165
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_1_2",
                "RadialLocation": 1,
                "TangentialLocation": 2,
                "Temperature": 78.00805503453113
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_1_3",
                "RadialLocation": 1,
                "TangentialLocation": 3,
                "Temperature": 78.45032662563871
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_1_4",
                "RadialLocation": 1,
                "TangentialLocation": 4,
                "Temperature": 78.44983682772944
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_1_5",
                "RadialLocation": 1,
                "TangentialLocation": 5,
                "Temperature": 77.98497917444317
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_1_6",
                "RadialLocation": 1,
                "TangentialLocation": 6,
                "Temperature": 76.98947969262085
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_1_7",
                "RadialLocation": 1,
                "TangentialLocation": 7,
                "Temperature": 75.29810941968908
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_1_8",
                "RadialLocation": 1,
                "TangentialLocation": 8,
                "Temperature": 72.44041046736358
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 77.10301731948775
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_2_1",
                "RadialLocation": 2,
                "TangentialLocation": 1,
                "Temperature": 78.5295898260845
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_2_2",
                "RadialLocation": 2,
                "TangentialLocation": 2,
                "Temperature": 79.57573665070424
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_2_3",
                "RadialLocation": 2,
                "TangentialLocation": 3,
                "Temperature": 80.10711130572251
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_2_4",
                "RadialLocation": 2,
                "TangentialLocation": 4,
                "Temperature": 80.11074722069006
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_2_5",
                "RadialLocation": 2,
                "TangentialLocation": 5,
                "Temperature": 79.5670257410493
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_2_6",
                "RadialLocation": 2,
                "TangentialLocation": 6,
                "Temperature": 78.40939506117337
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_2_7",
                "RadialLocation": 2,
                "TangentialLocation": 7,
                "Temperature": 76.47145938409807
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_2_8",
                "RadialLocation": 2,
                "TangentialLocation": 8,
                "Temperature": 73.27471941438151
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 77.87059513281679
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_3_1",
                "RadialLocation": 3,
                "TangentialLocation": 1,
                "Temperature": 79.52865405282797
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_3_2",
                "RadialLocation": 3,
                "TangentialLocation": 2,
                "Temperature": 80.71648226618646
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_3_3",
                "RadialLocation": 3,
                "TangentialLocation": 3,
                "Temperature": 81.31917166823763
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_3_4",
                "RadialLocation": 3,
                "TangentialLocation": 4,
                "Temperature": 81.32982810873831
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_3_5",
                "RadialLocation": 3,
                "TangentialLocation": 5,
                "Temperature": 80.73155139676155
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_3_6",
                "RadialLocation": 3,
                "TangentialLocation": 6,
                "Temperature": 79.45955312664643
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_3_7",
                "RadialLocation": 3,
                "TangentialLocation": 7,
                "Temperature": 77.34796248386512
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_3_8",
                "RadialLocation": 3,
                "TangentialLocation": 8,
                "Temperature": 73.90830356742116
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 78.41379487646523
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_4_1",
                "RadialLocation": 4,
                "TangentialLocation": 1,
                "Temperature": 80.2424612614048
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_4_2",
                "RadialLocation": 4,
                "TangentialLocation": 2,
                "Temperature": 81.53789860210638
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_4_3",
                "RadialLocation": 4,
                "TangentialLocation": 3,
                "Temperature": 82.19650884180425
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_4_4",
                "RadialLocation": 4,
                "TangentialLocation": 4,
                "Temperature": 82.21503553005152
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_4_5",
                "RadialLocation": 4,
                "TangentialLocation": 5,
                "Temperature": 81.57870624275945
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_4_6",
                "RadialLocation": 4,
                "TangentialLocation": 6,
                "Temperature": 80.22453571536872
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_4_7",
                "RadialLocation": 4,
                "TangentialLocation": 7,
                "Temperature": 77.98723832679153
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_4_8",
                "RadialLocation": 4,
                "TangentialLocation": 8,
                "Temperature": 74.37030988025602
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 78.79633989001294
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_5_1",
                "RadialLocation": 5,
                "TangentialLocation": 1,
                "Temperature": 80.74849431740708
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_5_2",
                "RadialLocation": 5,
                "TangentialLocation": 2,
                "Temperature": 82.12366422242388
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_5_3",
                "RadialLocation": 5,
                "TangentialLocation": 3,
                "Temperature": 82.82482747358345
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_5_4",
                "RadialLocation": 5,
                "TangentialLocation": 4,
                "Temperature": 82.85068434468442
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_5_5",
                "RadialLocation": 5,
                "TangentialLocation": 5,
                "Temperature": 82.18784241635286
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_5_6",
                "RadialLocation": 5,
                "TangentialLocation": 6,
                "Temperature": 80.7747070363526
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_5_7",
                "RadialLocation": 5,
                "TangentialLocation": 7,
                "Temperature": 78.4465150415011
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_5_8",
                "RadialLocation": 5,
                "TangentialLocation": 8,
                "Temperature": 74.70121254627341
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 79.0613530886894
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_6_1",
                "RadialLocation": 6,
                "TangentialLocation": 1,
                "Temperature": 81.10065640881018
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_6_2",
                "RadialLocation": 6,
                "TangentialLocation": 2,
                "Temperature": 82.53303998103748
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_6_3",
                "RadialLocation": 6,
                "TangentialLocation": 3,
                "Temperature": 83.26534770927772
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_6_4",
                "RadialLocation": 6,
                "TangentialLocation": 4,
                "Temperature": 83.29726129633386
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_6_5",
                "RadialLocation": 6,
                "TangentialLocation": 5,
                "Temperature": 82.61620406564514
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_6_6",
                "RadialLocation": 6,
                "TangentialLocation": 6,
                "Temperature": 81.1615538040454
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_6_7",
                "RadialLocation": 6,
                "TangentialLocation": 7,
                "Temperature": 78.76899485084748
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_6_8",
                "RadialLocation": 6,
                "TangentialLocation": 8,
                "Temperature": 74.93286685022204
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 79.23702598529913
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_7_1",
                "RadialLocation": 7,
                "TangentialLocation": 1,
                "Temperature": 81.33481242132474
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_7_2",
                "RadialLocation": 7,
                "TangentialLocation": 2,
                "Temperature": 82.80601436375633
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_7_3",
                "RadialLocation": 7,
                "TangentialLocation": 3,
                "Temperature": 83.55973003439611
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_7_4",
                "RadialLocation": 7,
                "TangentialLocation": 4,
                "Temperature": 83.59610582215508
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_7_5",
                "RadialLocation": 7,
                "TangentialLocation": 5,
                "Temperature": 82.90302270894905
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_7_6",
                "RadialLocation": 7,
                "TangentialLocation": 6,
                "Temperature": 81.42050065461825
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_7_7",
                "RadialLocation": 7,
                "TangentialLocation": 7,
                "Temperature": 78.98458011262241
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_7_8",
                "RadialLocation": 7,
                "TangentialLocation": 8,
                "Temperature": 75.08737291911744
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 79.34102558008358
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_8_1",
                "RadialLocation": 8,
                "TangentialLocation": 1,
                "Temperature": 81.47369843989325
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_8_2",
                "RadialLocation": 8,
                "TangentialLocation": 2,
                "Temperature": 82.9681945154027
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_8_3",
                "RadialLocation": 8,
                "TangentialLocation": 3,
                "Temperature": 83.73482863654267
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_8_4",
                "RadialLocation": 8,
                "TangentialLocation": 4,
                "Temperature": 83.77395433780188
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_8_5",
                "RadialLocation": 8,
                "TangentialLocation": 5,
                "Temperature": 83.07370100711105
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_8_6",
                "RadialLocation": 8,
                "TangentialLocation": 6,
                "Temperature": 81.57448563059738
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_8_7",
                "RadialLocation": 8,
                "TangentialLocation": 7,
                "Temperature": 79.11260758994479
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_8_8",
                "RadialLocation": 8,
                "TangentialLocation": 8,
                "Temperature": 75.17895217951244
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 79.38334351420373
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_9_1",
                "RadialLocation": 9,
                "TangentialLocation": 1,
                "Temperature": 81.5302689401439
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_9_2",
                "RadialLocation": 9,
                "TangentialLocation": 2,
                "Temperature": 83.03426651024222
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_9_3",
                "RadialLocation": 9,
                "TangentialLocation": 3,
                "Temperature": 83.80610680282044
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_9_4",
                "RadialLocation": 9,
                "TangentialLocation": 4,
                "Temperature": 83.84622199669104
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_9_5",
                "RadialLocation": 9,
                "TangentialLocation": 5,
                "Temperature": 83.14286975786436
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_9_6",
                "RadialLocation": 9,
                "TangentialLocation": 6,
                "Temperature": 81.63668274225758
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_9_7",
                "RadialLocation": 9,
                "TangentialLocation": 7,
                "Temperature": 79.16413358803017
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_9_8",
                "RadialLocation": 9,
                "TangentialLocation": 8,
                "Temperature": 75.21568524379289
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 79.36788738091859
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_10_1",
                "RadialLocation": 10,
                "TangentialLocation": 1,
                "Temperature": 81.50962084683633
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_10_2",
                "RadialLocation": 10,
                "TangentialLocation": 2,
                "Temperature": 83.01003095257053
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_10_3",
                "RadialLocation": 10,
                "TangentialLocation": 3,
                "Temperature": 83.77966924636866
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_10_4",
                "RadialLocation": 10,
                "TangentialLocation": 4,
                "Temperature": 83.81895965840098
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_10_5",
                "RadialLocation": 10,
                "TangentialLocation": 5,
                "Temperature": 83.11620964984677
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_10_6",
                "RadialLocation": 10,
                "TangentialLocation": 6,
                "Temperature": 81.612131762532
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_10_7",
                "RadialLocation": 10,
                "TangentialLocation": 7,
                "Temperature": 79.14331906522871
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_10_8",
                "RadialLocation": 10,
                "TangentialLocation": 8,
                "Temperature": 75.20057027662169
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 79.29308426461355
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_11_1",
                "RadialLocation": 11,
                "TangentialLocation": 1,
                "Temperature": 81.40974378043835
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_11_2",
                "RadialLocation": 11,
                "TangentialLocation": 2,
                "Temperature": 82.89321663390396
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_11_3",
                "RadialLocation": 11,
                "TangentialLocation": 3,
                "Temperature": 83.65308349890645
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_11_4",
                "RadialLocation": 11,
                "TangentialLocation": 4,
                "Temperature": 83.6896383452415
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_11_5",
                "RadialLocation": 11,
                "TangentialLocation": 5,
                "Temperature": 82.99116085038351
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_11_6",
                "RadialLocation": 11,
                "TangentialLocation": 6,
                "Temperature": 81.49834471055696
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_11_7",
                "RadialLocation": 11,
                "TangentialLocation": 7,
                "Temperature": 79.04791837859611
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_11_8",
                "RadialLocation": 11,
                "TangentialLocation": 8,
                "Temperature": 75.13188017993402
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 79.15162190853036
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_12_1",
                "RadialLocation": 12,
                "TangentialLocation": 1,
                "Temperature": 81.22123669372569
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_12_2",
                "RadialLocation": 12,
                "TangentialLocation": 2,
                "Temperature": 82.67321259569806
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_12_3",
                "RadialLocation": 12,
                "TangentialLocation": 3,
                "Temperature": 83.41512718821586
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_12_4",
                "RadialLocation": 12,
                "TangentialLocation": 4,
                "Temperature": 83.44688866593022
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_12_5",
                "RadialLocation": 12,
                "TangentialLocation": 5,
                "Temperature": 82.75662671414891
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_12_6",
                "RadialLocation": 12,
                "TangentialLocation": 6,
                "Temperature": 81.2849605972444
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_12_7",
                "RadialLocation": 12,
                "TangentialLocation": 7,
                "Temperature": 78.86890537948821
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_12_8",
                "RadialLocation": 12,
                "TangentialLocation": 8,
                "Temperature": 75.00283189939496
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 78.92931958201896
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_13_1",
                "RadialLocation": 13,
                "TangentialLocation": 1,
                "Temperature": 80.92602059943982
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_13_2",
                "RadialLocation": 13,
                "TangentialLocation": 2,
                "Temperature": 82.32979069953696
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_13_3",
                "RadialLocation": 13,
                "TangentialLocation": 3,
                "Temperature": 83.04456104476314
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_13_4",
                "RadialLocation": 13,
                "TangentialLocation": 4,
                "Temperature": 83.06929949757256
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_13_5",
                "RadialLocation": 13,
                "TangentialLocation": 5,
                "Temperature": 82.39175460709862
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_13_6",
                "RadialLocation": 13,
                "TangentialLocation": 6,
                "Temperature": 80.95248764830585
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_13_7",
                "RadialLocation": 13,
                "TangentialLocation": 7,
                "Temperature": 78.5892227552807
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_13_8",
                "RadialLocation": 13,
                "TangentialLocation": 8,
                "Temperature": 74.800518808398
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 78.60309989073028
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_14_1",
                "RadialLocation": 14,
                "TangentialLocation": 1,
                "Temperature": 80.49513941649725
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_14_2",
                "RadialLocation": 14,
                "TangentialLocation": 2,
                "Temperature": 81.83103627861148
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_14_3",
                "RadialLocation": 14,
                "TangentialLocation": 3,
                "Temperature": 82.50822428790613
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_14_4",
                "RadialLocation": 14,
                "TangentialLocation": 4,
                "Temperature": 82.52359407199353
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_14_5",
                "RadialLocation": 14,
                "TangentialLocation": 5,
                "Temperature": 81.86407775621204
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_14_6",
                "RadialLocation": 14,
                "TangentialLocation": 6,
                "Temperature": 80.4703312727323
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_14_7",
                "RadialLocation": 14,
                "TangentialLocation": 7,
                "Temperature": 78.18172885818002
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_14_8",
                "RadialLocation": 14,
                "TangentialLocation": 8,
                "Temperature": 74.50406480144684
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 78.13849909905004
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_15_1",
                "RadialLocation": 15,
                "TangentialLocation": 1,
                "Temperature": 79.88651231149524
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_15_2",
                "RadialLocation": 15,
                "TangentialLocation": 2,
                "Temperature": 81.13168389613756
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_15_3",
                "RadialLocation": 15,
                "TangentialLocation": 3,
                "Temperature": 81.75982809025629
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_15_4",
                "RadialLocation": 15,
                "TangentialLocation": 4,
                "Temperature": 81.76360141521876
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_15_5",
                "RadialLocation": 15,
                "TangentialLocation": 5,
                "Temperature": 81.12836231470827
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_15_6",
                "RadialLocation": 15,
                "TangentialLocation": 6,
                "Temperature": 79.79525967705659
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_15_7",
                "RadialLocation": 15,
                "TangentialLocation": 7,
                "Temperature": 77.60716929282039
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_15_8",
                "RadialLocation": 15,
                "TangentialLocation": 8,
                "Temperature": 74.08240947271914
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 77.48979633045785
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_16_1",
                "RadialLocation": 16,
                "TangentialLocation": 1,
                "Temperature": 79.0471871739764
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_16_2",
                "RadialLocation": 16,
                "TangentialLocation": 2,
                "Temperature": 80.17727639015527
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_16_3",
                "RadialLocation": 16,
                "TangentialLocation": 3,
                "Temperature": 80.74524270839841
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_16_4",
                "RadialLocation": 16,
                "TangentialLocation": 4,
                "Temperature": 80.73587691385876
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_16_5",
                "RadialLocation": 16,
                "TangentialLocation": 5,
                "Temperature": 80.13183206255185
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_16_6",
                "RadialLocation": 16,
                "TangentialLocation": 6,
                "Temperature": 78.87552502841933
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_16_7",
                "RadialLocation": 16,
                "TangentialLocation": 7,
                "Temperature": 76.81652035797612
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_16_8",
                "RadialLocation": 16,
                "TangentialLocation": 8,
                "Temperature": 73.49461436259216
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 76.61941458531929
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_17_1",
                "RadialLocation": 17,
                "TangentialLocation": 1,
                "Temperature": 77.94190441211165
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_17_2",
                "RadialLocation": 17,
                "TangentialLocation": 2,
                "Temperature": 78.93828675154568
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_17_3",
                "RadialLocation": 17,
                "TangentialLocation": 3,
                "Temperature": 79.43924876234007
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_17_4",
                "RadialLocation": 17,
                "TangentialLocation": 4,
                "Temperature": 79.41697822397383
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_17_5",
                "RadialLocation": 17,
                "TangentialLocation": 5,
                "Temperature": 78.85023084091534
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_17_6",
                "RadialLocation": 17,
                "TangentialLocation": 6,
                "Temperature": 77.68384163834038
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_17_7",
                "RadialLocation": 17,
                "TangentialLocation": 7,
                "Temperature": 75.77835879244462
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_17_8",
                "RadialLocation": 17,
                "TangentialLocation": 8,
                "Temperature": 72.708136008633
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 75.63471294568794
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_18_1",
                "RadialLocation": 18,
                "TangentialLocation": 1,
                "Temperature": 76.72582151996446
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_18_2",
                "RadialLocation": 18,
                "TangentialLocation": 2,
                "Temperature": 77.59954154931414
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_18_3",
                "RadialLocation": 18,
                "TangentialLocation": 3,
                "Temperature": 78.04176614977801
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_18_4",
                "RadialLocation": 18,
                "TangentialLocation": 4,
                "Temperature": 78.0103165656945
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_18_5",
                "RadialLocation": 18,
                "TangentialLocation": 5,
                "Temperature": 77.48011690598179
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_18_6",
                "RadialLocation": 18,
                "TangentialLocation": 6,
                "Temperature": 76.39922618170971
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_18_7",
                "RadialLocation": 18,
                "TangentialLocation": 7,
                "Temperature": 74.64126303339144
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "RotorWinding-Leading_Core_1_18_8",
                "RadialLocation": 18,
                "TangentialLocation": 8,
                "Temperature": 71.82372133495019
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 76.3302512549226
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_0_1",
                "RadialLocation": 0,
                "TangentialLocation": 1,
                "Temperature": 76.80345977832779
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_0_2",
                "RadialLocation": 0,
                "TangentialLocation": 2,
                "Temperature": 77.28072271165136
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_0_3",
                "RadialLocation": 0,
                "TangentialLocation": 3,
                "Temperature": 77.53832794161951
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_0_4",
                "RadialLocation": 0,
                "TangentialLocation": 4,
                "Temperature": 77.52399200119442
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_0_5",
                "RadialLocation": 0,
                "TangentialLocation": 5,
                "Temperature": 77.21132650592004
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_0_6",
                "RadialLocation": 0,
                "TangentialLocation": 6,
                "Temperature": 76.55300466533983
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_0_7",
                "RadialLocation": 0,
                "TangentialLocation": 7,
                "Temperature": 75.43708621288333
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_0_8",
                "RadialLocation": 0,
                "TangentialLocation": 8,
                "Temperature": 73.56150987366676
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 77.49914110104503
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_1_1",
                "RadialLocation": 1,
                "TangentialLocation": 1,
                "Temperature": 78.30447337058408
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_1_2",
                "RadialLocation": 1,
                "TangentialLocation": 2,
                "Temperature": 78.98982411919337
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_1_3",
                "RadialLocation": 1,
                "TangentialLocation": 3,
                "Temperature": 79.34979933837887
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_1_4",
                "RadialLocation": 1,
                "TangentialLocation": 4,
                "Temperature": 79.33140822783164
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_1_5",
                "RadialLocation": 1,
                "TangentialLocation": 5,
                "Temperature": 78.90431539107291
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_1_6",
                "RadialLocation": 1,
                "TangentialLocation": 6,
                "Temperature": 78.01410341954578
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_1_7",
                "RadialLocation": 1,
                "TangentialLocation": 7,
                "Temperature": 76.5401554552705
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_1_8",
                "RadialLocation": 1,
                "TangentialLocation": 8,
                "Temperature": 74.1901637151404
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 78.41020731928081
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_2_1",
                "RadialLocation": 2,
                "TangentialLocation": 1,
                "Temperature": 79.49778563057482
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_2_2",
                "RadialLocation": 2,
                "TangentialLocation": 2,
                "Temperature": 80.35218362996288
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_2_3",
                "RadialLocation": 2,
                "TangentialLocation": 3,
                "Temperature": 80.7943133454579
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_2_4",
                "RadialLocation": 2,
                "TangentialLocation": 4,
                "Temperature": 80.77794620256624
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_2_5",
                "RadialLocation": 2,
                "TangentialLocation": 5,
                "Temperature": 80.27429970883374
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_2_6",
                "RadialLocation": 2,
                "TangentialLocation": 6,
                "Temperature": 79.22921239443554
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_2_7",
                "RadialLocation": 2,
                "TangentialLocation": 7,
                "Temperature": 77.52259515162983
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_2_8",
                "RadialLocation": 2,
                "TangentialLocation": 8,
                "Temperature": 74.86069766979273
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 79.08427979734977
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_3_1",
                "RadialLocation": 3,
                "TangentialLocation": 1,
                "Temperature": 80.39215352315898
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_3_2",
                "RadialLocation": 3,
                "TangentialLocation": 2,
                "Temperature": 81.38137158943424
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_3_3",
                "RadialLocation": 3,
                "TangentialLocation": 3,
                "Temperature": 81.89079349374583
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_3_4",
                "RadialLocation": 3,
                "TangentialLocation": 4,
                "Temperature": 81.8803002427023
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_3_5",
                "RadialLocation": 3,
                "TangentialLocation": 5,
                "Temperature": 81.32379889067191
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_3_6",
                "RadialLocation": 3,
                "TangentialLocation": 6,
                "Temperature": 80.168938967152
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_3_7",
                "RadialLocation": 3,
                "TangentialLocation": 7,
                "Temperature": 78.29619851977539
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_3_8",
                "RadialLocation": 3,
                "TangentialLocation": 8,
                "Temperature": 75.40391096485178
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 79.57375594354474
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_4_1",
                "RadialLocation": 4,
                "TangentialLocation": 1,
                "Temperature": 81.04737934262616
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_4_2",
                "RadialLocation": 4,
                "TangentialLocation": 2,
                "Temperature": 82.14081746657179
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_4_3",
                "RadialLocation": 4,
                "TangentialLocation": 3,
                "Temperature": 82.70394542252308
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_4_4",
                "RadialLocation": 4,
                "TangentialLocation": 4,
                "Temperature": 82.70070889296598
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_4_5",
                "RadialLocation": 4,
                "TangentialLocation": 5,
                "Temperature": 82.1072370125371
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_4_6",
                "RadialLocation": 4,
                "TangentialLocation": 6,
                "Temperature": 80.87285435943144
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_4_7",
                "RadialLocation": 4,
                "TangentialLocation": 7,
                "Temperature": 78.878162813271
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_4_8",
                "RadialLocation": 4,
                "TangentialLocation": 8,
                "Temperature": 75.81396116826564
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 79.92463426742698
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_5_1",
                "RadialLocation": 5,
                "TangentialLocation": 1,
                "Temperature": 81.51995451837817
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_5_2",
                "RadialLocation": 5,
                "TangentialLocation": 2,
                "Temperature": 82.69160246883655
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_5_3",
                "RadialLocation": 5,
                "TangentialLocation": 3,
                "Temperature": 83.29613019695637
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_5_4",
                "RadialLocation": 5,
                "TangentialLocation": 4,
                "Temperature": 83.29990383793901
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_5_5",
                "RadialLocation": 5,
                "TangentialLocation": 5,
                "Temperature": 82.68054557034785
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_5_6",
                "RadialLocation": 5,
                "TangentialLocation": 6,
                "Temperature": 81.38860993982648
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_5_7",
                "RadialLocation": 5,
                "TangentialLocation": 7,
                "Temperature": 79.30469730358557
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_5_8",
                "RadialLocation": 5,
                "TangentialLocation": 8,
                "Temperature": 76.11403488438417
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 80.17076813242404
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_6_1",
                "RadialLocation": 6,
                "TangentialLocation": 1,
                "Temperature": 81.85284386671972
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_6_2",
                "RadialLocation": 6,
                "TangentialLocation": 2,
                "Temperature": 83.08112884729478
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_6_3",
                "RadialLocation": 6,
                "TangentialLocation": 3,
                "Temperature": 83.71623916941863
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_6_4",
                "RadialLocation": 6,
                "TangentialLocation": 4,
                "Temperature": 83.72590893698592
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_6_5",
                "RadialLocation": 6,
                "TangentialLocation": 5,
                "Temperature": 83.08867315796587
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_6_6",
                "RadialLocation": 6,
                "TangentialLocation": 6,
                "Temperature": 81.75591943189485
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_6_7",
                "RadialLocation": 6,
                "TangentialLocation": 7,
                "Temperature": 79.60825423917095
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_6_8",
                "RadialLocation": 6,
                "TangentialLocation": 8,
                "Temperature": 76.3271349977128
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 80.33536635923615
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_7_1",
                "RadialLocation": 7,
                "TangentialLocation": 1,
                "Temperature": 82.07607583305057
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_7_2",
                "RadialLocation": 7,
                "TangentialLocation": 2,
                "Temperature": 83.34303833979213
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_7_3",
                "RadialLocation": 7,
                "TangentialLocation": 3,
                "Temperature": 83.99930785055169
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_7_4",
                "RadialLocation": 7,
                "TangentialLocation": 4,
                "Temperature": 84.01336453877433
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_7_5",
                "RadialLocation": 7,
                "TangentialLocation": 5,
                "Temperature": 83.36427275948532
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_7_6",
                "RadialLocation": 7,
                "TangentialLocation": 6,
                "Temperature": 82.00395966011322
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_7_7",
                "RadialLocation": 7,
                "TangentialLocation": 7,
                "Temperature": 79.81306576328379
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_7_8",
                "RadialLocation": 7,
                "TangentialLocation": 8,
                "Temperature": 76.47065271406528
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 80.43341307041739
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_8_1",
                "RadialLocation": 8,
                "TangentialLocation": 1,
                "Temperature": 82.20927435538943
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_8_2",
                "RadialLocation": 8,
                "TangentialLocation": 2,
                "Temperature": 83.49955395984094
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_8_3",
                "RadialLocation": 8,
                "TangentialLocation": 3,
                "Temperature": 84.16865074538545
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_8_4",
                "RadialLocation": 8,
                "TangentialLocation": 4,
                "Temperature": 84.18542742106294
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_8_5",
                "RadialLocation": 8,
                "TangentialLocation": 5,
                "Temperature": 83.5292418436166
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_8_6",
                "RadialLocation": 8,
                "TangentialLocation": 6,
                "Temperature": 82.15235433679074
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_8_7",
                "RadialLocation": 8,
                "TangentialLocation": 7,
                "Temperature": 79.93546403856439
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_8_8",
                "RadialLocation": 8,
                "TangentialLocation": 8,
                "Temperature": 76.55628447393487
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 80.47355327836847
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_9_1",
                "RadialLocation": 9,
                "TangentialLocation": 1,
                "Temperature": 82.26384851263153
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_9_2",
                "RadialLocation": 9,
                "TangentialLocation": 2,
                "Temperature": 83.56368486430034
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_9_3",
                "RadialLocation": 9,
                "TangentialLocation": 3,
                "Temperature": 84.23797622282339
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_9_4",
                "RadialLocation": 9,
                "TangentialLocation": 4,
                "Temperature": 84.25573826401421
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_9_5",
                "RadialLocation": 9,
                "TangentialLocation": 5,
                "Temperature": 83.59647651796836
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_9_6",
                "RadialLocation": 9,
                "TangentialLocation": 6,
                "Temperature": 82.21264059368777
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_9_7",
                "RadialLocation": 9,
                "TangentialLocation": 7,
                "Temperature": 79.9850194282061
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_9_8",
                "RadialLocation": 9,
                "TangentialLocation": 8,
                "Temperature": 76.59084722105005
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 80.45923782809952
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_10_1",
                "RadialLocation": 10,
                "TangentialLocation": 1,
                "Temperature": 82.24438011399951
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_10_2",
                "RadialLocation": 10,
                "TangentialLocation": 2,
                "Temperature": 83.54067610543149
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_10_3",
                "RadialLocation": 10,
                "TangentialLocation": 3,
                "Temperature": 84.21280853774493
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_10_4",
                "RadialLocation": 10,
                "TangentialLocation": 4,
                "Temperature": 84.22976163227253
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_10_5",
                "RadialLocation": 10,
                "TangentialLocation": 5,
                "Temperature": 83.57108532022161
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_10_6",
                "RadialLocation": 10,
                "TangentialLocation": 6,
                "Temperature": 82.18931920120947
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_10_7",
                "RadialLocation": 10,
                "TangentialLocation": 7,
                "Temperature": 79.96540275204404
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_10_8",
                "RadialLocation": 10,
                "TangentialLocation": 8,
                "Temperature": 76.57691756058566
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 80.38918760066223
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_11_1",
                "RadialLocation": 11,
                "TangentialLocation": 1,
                "Temperature": 82.14920728392688
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_11_2",
                "RadialLocation": 11,
                "TangentialLocation": 2,
                "Temperature": 83.42863977162146
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_11_3",
                "RadialLocation": 11,
                "TangentialLocation": 3,
                "Temperature": 84.09111838913687
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_11_4",
                "RadialLocation": 11,
                "TangentialLocation": 4,
                "Temperature": 84.10537730356374
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_11_5",
                "RadialLocation": 11,
                "TangentialLocation": 5,
                "Temperature": 83.45090904011732
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_11_6",
                "RadialLocation": 11,
                "TangentialLocation": 6,
                "Temperature": 82.08028132395
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_11_7",
                "RadialLocation": 11,
                "TangentialLocation": 7,
                "Temperature": 79.87471324127486
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_11_8",
                "RadialLocation": 11,
                "TangentialLocation": 8,
                "Temperature": 76.51306074219362
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 80.25724466116249
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_12_1",
                "RadialLocation": 12,
                "TangentialLocation": 1,
                "Temperature": 81.97027510627755
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_12_2",
                "RadialLocation": 12,
                "TangentialLocation": 2,
                "Temperature": 83.21843396878646
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_12_3",
                "RadialLocation": 12,
                "TangentialLocation": 3,
                "Temperature": 83.86322302982927
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_12_4",
                "RadialLocation": 12,
                "TangentialLocation": 4,
                "Temperature": 83.87277335513761
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_12_5",
                "RadialLocation": 12,
                "TangentialLocation": 5,
                "Temperature": 83.22637461822461
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_12_6",
                "RadialLocation": 12,
                "TangentialLocation": 6,
                "Temperature": 81.87660537725837
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_12_7",
                "RadialLocation": 12,
                "TangentialLocation": 7,
                "Temperature": 79.70523276355732
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_12_8",
                "RadialLocation": 12,
                "TangentialLocation": 8,
                "Temperature": 76.39360425178498
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 80.05166145795957
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_13_1",
                "RadialLocation": 13,
                "TangentialLocation": 1,
                "Temperature": 81.69235461972781
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_13_2",
                "RadialLocation": 13,
                "TangentialLocation": 2,
                "Temperature": 82.89293852838402
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_13_3",
                "RadialLocation": 13,
                "TangentialLocation": 3,
                "Temperature": 83.51113400665646
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_13_4",
                "RadialLocation": 13,
                "TangentialLocation": 4,
                "Temperature": 83.5138228556531
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_13_5",
                "RadialLocation": 13,
                "TangentialLocation": 5,
                "Temperature": 82.8798413820752
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_13_6",
                "RadialLocation": 13,
                "TangentialLocation": 6,
                "Temperature": 81.56183434090106
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_13_7",
                "RadialLocation": 13,
                "TangentialLocation": 7,
                "Temperature": 79.44265637191366
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_13_8",
                "RadialLocation": 13,
                "TangentialLocation": 8,
                "Temperature": 76.2079584076748
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 79.75401725856011
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_14_1",
                "RadialLocation": 14,
                "TangentialLocation": 1,
                "Temperature": 81.29198423159256
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_14_2",
                "RadialLocation": 14,
                "TangentialLocation": 2,
                "Temperature": 82.42622425532588
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_14_3",
                "RadialLocation": 14,
                "TangentialLocation": 3,
                "Temperature": 83.0079333217541
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_14_4",
                "RadialLocation": 14,
                "TangentialLocation": 4,
                "Temperature": 83.00154528125987
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_14_5",
                "RadialLocation": 14,
                "TangentialLocation": 5,
                "Temperature": 82.38500083961497
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_14_6",
                "RadialLocation": 14,
                "TangentialLocation": 6,
                "Temperature": 81.11119716051961
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_14_7",
                "RadialLocation": 14,
                "TangentialLocation": 7,
                "Temperature": 79.06511503425628
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_14_8",
                "RadialLocation": 14,
                "TangentialLocation": 8,
                "Temperature": 75.93963586302053
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 79.33872494246151
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_15_1",
                "RadialLocation": 15,
                "TangentialLocation": 1,
                "Temperature": 80.73761977204447
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_15_2",
                "RadialLocation": 15,
                "TangentialLocation": 2,
                "Temperature": 81.78446812339513
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_15_3",
                "RadialLocation": 15,
                "TangentialLocation": 3,
                "Temperature": 82.31921649303938
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_15_4",
                "RadialLocation": 15,
                "TangentialLocation": 4,
                "Temperature": 82.30172939314693
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_15_5",
                "RadialLocation": 15,
                "TangentialLocation": 5,
                "Temperature": 81.70832007033653
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_15_6",
                "RadialLocation": 15,
                "TangentialLocation": 6,
                "Temperature": 80.49254587166813
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_15_7",
                "RadialLocation": 15,
                "TangentialLocation": 7,
                "Temperature": 78.54338523184701
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_15_8",
                "RadialLocation": 15,
                "TangentialLocation": 8,
                "Temperature": 75.565834954199
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 78.77734065578264
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_16_1",
                "RadialLocation": 16,
                "TangentialLocation": 1,
                "Temperature": 79.99684003159398
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_16_2",
                "RadialLocation": 16,
                "TangentialLocation": 2,
                "Temperature": 80.935367995333
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_16_3",
                "RadialLocation": 16,
                "TangentialLocation": 3,
                "Temperature": 81.4137364072098
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_16_4",
                "RadialLocation": 16,
                "TangentialLocation": 4,
                "Temperature": 81.38389682596366
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_16_5",
                "RadialLocation": 16,
                "TangentialLocation": 5,
                "Temperature": 80.81949780579455
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_16_6",
                "RadialLocation": 16,
                "TangentialLocation": 6,
                "Temperature": 79.675470774778
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_16_7",
                "RadialLocation": 16,
                "TangentialLocation": 7,
                "Temperature": 77.84777846239923
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_16_8",
                "RadialLocation": 16,
                "TangentialLocation": 8,
                "Temperature": 75.06140656008688
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 78.0654478582637
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_17_1",
                "RadialLocation": 17,
                "TangentialLocation": 1,
                "Temperature": 79.07345177580477
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_17_2",
                "RadialLocation": 17,
                "TangentialLocation": 2,
                "Temperature": 79.89111777402942
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_17_3",
                "RadialLocation": 17,
                "TangentialLocation": 3,
                "Temperature": 80.30907902859602
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_17_4",
                "RadialLocation": 17,
                "TangentialLocation": 4,
                "Temperature": 80.26743611792996
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_17_5",
                "RadialLocation": 17,
                "TangentialLocation": 5,
                "Temperature": 79.73618122818483
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_17_6",
                "RadialLocation": 17,
                "TangentialLocation": 6,
                "Temperature": 78.67254472641888
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_17_7",
                "RadialLocation": 17,
                "TangentialLocation": 7,
                "Temperature": 76.98306857964268
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_17_8",
                "RadialLocation": 17,
                "TangentialLocation": 8,
                "Temperature": 74.42325520094852
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 77.34715019378548
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_18_1",
                "RadialLocation": 18,
                "TangentialLocation": 1,
                "Temperature": 78.16437482743837
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_18_2",
                "RadialLocation": 18,
                "TangentialLocation": 2,
                "Temperature": 78.88009950844537
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_18_3",
                "RadialLocation": 18,
                "TangentialLocation": 3,
                "Temperature": 79.24927721585202
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_18_4",
                "RadialLocation": 18,
                "TangentialLocation": 4,
                "Temperature": 79.19961615307221
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_18_5",
                "RadialLocation": 18,
                "TangentialLocation": 5,
                "Temperature": 78.6977285089591
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_18_6",
                "RadialLocation": 18,
                "TangentialLocation": 6,
                "Temperature": 77.70349092903277
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_18_7",
                "RadialLocation": 18,
                "TangentialLocation": 7,
                "Temperature": 76.13476947402452
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "RotorWinding-Leading_Core_2_18_8",
                "RadialLocation": 18,
                "TangentialLocation": 8,
                "Temperature": 73.78197205260572
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 77.94049007371453
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_0_1",
                "RadialLocation": 0,
                "TangentialLocation": 1,
                "Temperature": 78.22631744581837
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_0_2",
                "RadialLocation": 0,
                "TangentialLocation": 2,
                "Temperature": 78.57825378510599
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_0_3",
                "RadialLocation": 0,
                "TangentialLocation": 3,
                "Temperature": 78.77499827750283
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_0_4",
                "RadialLocation": 0,
                "TangentialLocation": 4,
                "Temperature": 78.74876513797597
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_0_5",
                "RadialLocation": 0,
                "TangentialLocation": 5,
                "Temperature": 78.46946580805093
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_0_6",
                "RadialLocation": 0,
                "TangentialLocation": 6,
                "Temperature": 77.90240442358672
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_0_7",
                "RadialLocation": 0,
                "TangentialLocation": 7,
                "Temperature": 76.98123011852412
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_0_8",
                "RadialLocation": 0,
                "TangentialLocation": 8,
                "Temperature": 75.56657760275674
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 78.84252945134358
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_1_1",
                "RadialLocation": 1,
                "TangentialLocation": 1,
                "Temperature": 79.40202870123451
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_1_2",
                "RadialLocation": 1,
                "TangentialLocation": 2,
                "Temperature": 79.93162059634422
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_1_3",
                "RadialLocation": 1,
                "TangentialLocation": 3,
                "Temperature": 80.21606810577222
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_1_4",
                "RadialLocation": 1,
                "TangentialLocation": 4,
                "Temperature": 80.1821430308375
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_1_5",
                "RadialLocation": 1,
                "TangentialLocation": 5,
                "Temperature": 79.79475856412205
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_1_6",
                "RadialLocation": 1,
                "TangentialLocation": 6,
                "Temperature": 79.01473407063179
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_1_7",
                "RadialLocation": 1,
                "TangentialLocation": 7,
                "Temperature": 77.7753165938255
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_1_8",
                "RadialLocation": 1,
                "TangentialLocation": 8,
                "Temperature": 75.96700126943799
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 79.60239063256542
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_2_1",
                "RadialLocation": 2,
                "TangentialLocation": 1,
                "Temperature": 80.4131542142019
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_2_2",
                "RadialLocation": 2,
                "TangentialLocation": 2,
                "Temperature": 81.09576721061948
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_2_3",
                "RadialLocation": 2,
                "TangentialLocation": 3,
                "Temperature": 81.45432003552598
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_2_4",
                "RadialLocation": 2,
                "TangentialLocation": 4,
                "Temperature": 81.42035979555084
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_2_5",
                "RadialLocation": 2,
                "TangentialLocation": 5,
                "Temperature": 80.95991803268002
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_2_6",
                "RadialLocation": 2,
                "TangentialLocation": 6,
                "Temperature": 80.034949145378
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_2_7",
                "RadialLocation": 2,
                "TangentialLocation": 7,
                "Temperature": 78.58191854576181
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_2_8",
                "RadialLocation": 2,
                "TangentialLocation": 8,
                "Temperature": 76.49795024138992
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 80.19123956095106
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_3_1",
                "RadialLocation": 3,
                "TangentialLocation": 1,
                "Temperature": 81.20585187102549
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_3_2",
                "RadialLocation": 3,
                "TangentialLocation": 2,
                "Temperature": 82.01440608974806
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_3_3",
                "RadialLocation": 3,
                "TangentialLocation": 3,
                "Temperature": 82.43553821311819
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_3_4",
                "RadialLocation": 3,
                "TangentialLocation": 4,
                "Temperature": 82.40626000380199
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_3_5",
                "RadialLocation": 3,
                "TangentialLocation": 5,
                "Temperature": 81.89515879516631
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_3_6",
                "RadialLocation": 3,
                "TangentialLocation": 6,
                "Temperature": 80.86622675698911
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_3_7",
                "RadialLocation": 3,
                "TangentialLocation": 7,
                "Temperature": 79.25726872483564
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_3_8",
                "RadialLocation": 3,
                "TangentialLocation": 8,
                "Temperature": 76.96130339620908
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 80.6317767114918
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_4_1",
                "RadialLocation": 4,
                "TangentialLocation": 1,
                "Temperature": 81.80352663631751
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_4_2",
                "RadialLocation": 4,
                "TangentialLocation": 2,
                "Temperature": 82.71147170214192
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_4_3",
                "RadialLocation": 4,
                "TangentialLocation": 3,
                "Temperature": 83.18359902342372
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_4_4",
                "RadialLocation": 4,
                "TangentialLocation": 4,
                "Temperature": 83.1608917214394
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_4_5",
                "RadialLocation": 4,
                "TangentialLocation": 5,
                "Temperature": 82.61415258439783
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_4_6",
                "RadialLocation": 4,
                "TangentialLocation": 6,
                "Temperature": 81.50904268978665
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_4_7",
                "RadialLocation": 4,
                "TangentialLocation": 7,
                "Temperature": 79.78358331225927
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_4_8",
                "RadialLocation": 4,
                "TangentialLocation": 8,
                "Temperature": 77.3251649673673
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 80.95406899431698
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_5_1",
                "RadialLocation": 5,
                "TangentialLocation": 1,
                "Temperature": 82.24311263805507
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_5_2",
                "RadialLocation": 5,
                "TangentialLocation": 2,
                "Temperature": 83.22673049735398
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_5_3",
                "RadialLocation": 5,
                "TangentialLocation": 3,
                "Temperature": 83.73874686737757
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_5_4",
                "RadialLocation": 5,
                "TangentialLocation": 4,
                "Temperature": 83.72266174016751
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_5_5",
                "RadialLocation": 5,
                "TangentialLocation": 5,
                "Temperature": 83.15080806422766
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_5_6",
                "RadialLocation": 5,
                "TangentialLocation": 6,
                "Temperature": 81.99000427371959
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_5_7",
                "RadialLocation": 5,
                "TangentialLocation": 7,
                "Temperature": 80.17814761016575
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_5_8",
                "RadialLocation": 5,
                "TangentialLocation": 8,
                "Temperature": 77.59805269206281
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 81.18339849357032
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_6_1",
                "RadialLocation": 6,
                "TangentialLocation": 1,
                "Temperature": 82.55703066167506
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_6_2",
                "RadialLocation": 6,
                "TangentialLocation": 2,
                "Temperature": 83.59601363205499
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_6_3",
                "RadialLocation": 6,
                "TangentialLocation": 3,
                "Temperature": 84.13780151723786
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_6_4",
                "RadialLocation": 6,
                "TangentialLocation": 4,
                "Temperature": 84.12739881568224
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_6_5",
                "RadialLocation": 6,
                "TangentialLocation": 5,
                "Temperature": 83.53809587375764
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_6_6",
                "RadialLocation": 6,
                "TangentialLocation": 6,
                "Temperature": 82.33746705749007
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_6_7",
                "RadialLocation": 6,
                "TangentialLocation": 7,
                "Temperature": 80.46325322751349
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_6_8",
                "RadialLocation": 6,
                "TangentialLocation": 8,
                "Temperature": 77.79503374955631
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 81.33829672125705
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_7_1",
                "RadialLocation": 7,
                "TangentialLocation": 1,
                "Temperature": 82.76956158225573
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_7_2",
                "RadialLocation": 7,
                "TangentialLocation": 2,
                "Temperature": 83.84662730022023
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_7_3",
                "RadialLocation": 7,
                "TangentialLocation": 3,
                "Temperature": 84.40916141523954
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_7_4",
                "RadialLocation": 7,
                "TangentialLocation": 4,
                "Temperature": 84.40303345522936
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_7_5",
                "RadialLocation": 7,
                "TangentialLocation": 5,
                "Temperature": 83.80210060140736
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_7_6",
                "RadialLocation": 7,
                "TangentialLocation": 6,
                "Temperature": 82.5744157723749
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_7_7",
                "RadialLocation": 7,
                "TangentialLocation": 7,
                "Temperature": 80.65761518905897
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_7_8",
                "RadialLocation": 7,
                "TangentialLocation": 8,
                "Temperature": 77.92916896762732
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 81.43121193246682
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_8_1",
                "RadialLocation": 8,
                "TangentialLocation": 1,
                "Temperature": 82.89722437643461
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_8_2",
                "RadialLocation": 8,
                "TangentialLocation": 2,
                "Temperature": 83.99736553833456
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_8_3",
                "RadialLocation": 8,
                "TangentialLocation": 3,
                "Temperature": 84.57253963974773
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_8_4",
                "RadialLocation": 8,
                "TangentialLocation": 4,
                "Temperature": 84.56907959417704
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_8_5",
                "RadialLocation": 8,
                "TangentialLocation": 5,
                "Temperature": 83.96116124572468
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_8_6",
                "RadialLocation": 8,
                "TangentialLocation": 6,
                "Temperature": 82.71713140398391
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_8_7",
                "RadialLocation": 8,
                "TangentialLocation": 7,
                "Temperature": 80.77459175786488
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_8_8",
                "RadialLocation": 8,
                "TangentialLocation": 8,
                "Temperature": 78.00980667630964
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 81.46951416196559
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_9_1",
                "RadialLocation": 9,
                "TangentialLocation": 1,
                "Temperature": 82.9498749825567
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_9_2",
                "RadialLocation": 9,
                "TangentialLocation": 2,
                "Temperature": 84.0595224963402
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_9_3",
                "RadialLocation": 9,
                "TangentialLocation": 3,
                "Temperature": 84.63984117289843
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_9_4",
                "RadialLocation": 9,
                "TangentialLocation": 4,
                "Temperature": 84.6373534117341
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_9_5",
                "RadialLocation": 9,
                "TangentialLocation": 5,
                "Temperature": 84.02639402805967
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_9_6",
                "RadialLocation": 9,
                "TangentialLocation": 6,
                "Temperature": 82.77548234956933
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_9_7",
                "RadialLocation": 9,
                "TangentialLocation": 7,
                "Temperature": 80.82226857021743
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_9_8",
                "RadialLocation": 9,
                "TangentialLocation": 8,
                "Temperature": 78.04258432017994
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 81.45622286612246
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_10_1",
                "RadialLocation": 10,
                "TangentialLocation": 1,
                "Temperature": 82.93157476094044
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_10_2",
                "RadialLocation": 10,
                "TangentialLocation": 2,
                "Temperature": 84.037770317303
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_10_3",
                "RadialLocation": 10,
                "TangentialLocation": 3,
                "Temperature": 84.61598820796772
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_10_4",
                "RadialLocation": 10,
                "TangentialLocation": 4,
                "Temperature": 84.61271087514356
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_10_5",
                "RadialLocation": 10,
                "TangentialLocation": 5,
                "Temperature": 84.00231489588997
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_10_6",
                "RadialLocation": 10,
                "TangentialLocation": 6,
                "Temperature": 82.75341507325317
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_10_7",
                "RadialLocation": 10,
                "TangentialLocation": 7,
                "Temperature": 80.80382344546162
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_10_8",
                "RadialLocation": 10,
                "TangentialLocation": 8,
                "Temperature": 78.02968474363286
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 81.39033787129561
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_11_1",
                "RadialLocation": 11,
                "TangentialLocation": 1,
                "Temperature": 82.84100818260256
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_11_2",
                "RadialLocation": 11,
                "TangentialLocation": 2,
                "Temperature": 83.93060666714969
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_11_3",
                "RadialLocation": 11,
                "TangentialLocation": 3,
                "Temperature": 84.49935833969995
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_11_4",
                "RadialLocation": 11,
                "TangentialLocation": 4,
                "Temperature": 84.49344470641866
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_11_5",
                "RadialLocation": 11,
                "TangentialLocation": 5,
                "Temperature": 83.8871692353533
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_11_6",
                "RadialLocation": 11,
                "TangentialLocation": 6,
                "Temperature": 82.64920222879569
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_11_7",
                "RadialLocation": 11,
                "TangentialLocation": 7,
                "Temperature": 80.71769693332782
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_11_8",
                "RadialLocation": 11,
                "TangentialLocation": 8,
                "Temperature": 77.96994487728584
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 81.2667887396707
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_12_1",
                "RadialLocation": 12,
                "TangentialLocation": 1,
                "Temperature": 82.67145608639402
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_12_2",
                "RadialLocation": 12,
                "TangentialLocation": 2,
                "Temperature": 83.7303686057419
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_12_3",
                "RadialLocation": 12,
                "TangentialLocation": 3,
                "Temperature": 84.28182497696332
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_12_4",
                "RadialLocation": 12,
                "TangentialLocation": 4,
                "Temperature": 84.27131866218855
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_12_5",
                "RadialLocation": 12,
                "TangentialLocation": 5,
                "Temperature": 83.67292414348074
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_12_6",
                "RadialLocation": 12,
                "TangentialLocation": 6,
                "Temperature": 82.45537083144428
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_12_7",
                "RadialLocation": 12,
                "TangentialLocation": 7,
                "Temperature": 80.55746449461832
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_12_8",
                "RadialLocation": 12,
                "TangentialLocation": 8,
                "Temperature": 77.85872194333773
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 81.07609726835665
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_13_1",
                "RadialLocation": 13,
                "TangentialLocation": 1,
                "Temperature": 82.41047862801176
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_13_2",
                "RadialLocation": 13,
                "TangentialLocation": 2,
                "Temperature": 83.42301754681931
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_13_3",
                "RadialLocation": 13,
                "TangentialLocation": 3,
                "Temperature": 83.94863431577163
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_13_4",
                "RadialLocation": 13,
                "TangentialLocation": 4,
                "Temperature": 83.93147655235285
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_13_5",
                "RadialLocation": 13,
                "TangentialLocation": 5,
                "Temperature": 83.3451358081984
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_13_6",
                "RadialLocation": 13,
                "TangentialLocation": 6,
                "Temperature": 82.15847295948107
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_13_7",
                "RadialLocation": 13,
                "TangentialLocation": 7,
                "Temperature": 80.31150826480157
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_13_8",
                "RadialLocation": 13,
                "TangentialLocation": 8,
                "Temperature": 77.6875579191931
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 80.80409972120705
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_14_1",
                "RadialLocation": 14,
                "TangentialLocation": 1,
                "Temperature": 82.03985103466704
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_14_2",
                "RadialLocation": 14,
                "TangentialLocation": 2,
                "Temperature": 82.98839089615765
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_14_3",
                "RadialLocation": 14,
                "TangentialLocation": 3,
                "Temperature": 83.4788997644767
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_14_4",
                "RadialLocation": 14,
                "TangentialLocation": 4,
                "Temperature": 83.45302560700668
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_14_5",
                "RadialLocation": 14,
                "TangentialLocation": 5,
                "Temperature": 82.8834484056808
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_14_6",
                "RadialLocation": 14,
                "TangentialLocation": 6,
                "Temperature": 81.73935121955297
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_14_7",
                "RadialLocation": 14,
                "TangentialLocation": 7,
                "Temperature": 79.96297797972342
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_14_8",
                "RadialLocation": 14,
                "TangentialLocation": 8,
                "Temperature": 77.44393263450094
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 80.43300446176694
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_15_1",
                "RadialLocation": 15,
                "TangentialLocation": 1,
                "Temperature": 81.53760045042597
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_15_2",
                "RadialLocation": 15,
                "TangentialLocation": 2,
                "Temperature": 82.40314250151776
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_15_3",
                "RadialLocation": 15,
                "TangentialLocation": 3,
                "Temperature": 82.8491184789407
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_15_4",
                "RadialLocation": 15,
                "TangentialLocation": 4,
                "Temperature": 82.81273186818687
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_15_5",
                "RadialLocation": 15,
                "TangentialLocation": 5,
                "Temperature": 82.26506974648949
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_15_6",
                "RadialLocation": 15,
                "TangentialLocation": 6,
                "Temperature": 81.1760165467302
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_15_7",
                "RadialLocation": 15,
                "TangentialLocation": 7,
                "Temperature": 79.49175983927599
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_15_8",
                "RadialLocation": 15,
                "TangentialLocation": 8,
                "Temperature": 77.11223500377278
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 79.94830438592626
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_16_1",
                "RadialLocation": 16,
                "TangentialLocation": 1,
                "Temperature": 80.88827798511744
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_16_2",
                "RadialLocation": 16,
                "TangentialLocation": 2,
                "Temperature": 81.65336608455574
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_16_3",
                "RadialLocation": 16,
                "TangentialLocation": 3,
                "Temperature": 82.04705247964452
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_16_4",
                "RadialLocation": 16,
                "TangentialLocation": 4,
                "Temperature": 81.99919963872692
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_16_5",
                "RadialLocation": 16,
                "TangentialLocation": 5,
                "Temperature": 81.4783818378538
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_16_6",
                "RadialLocation": 16,
                "TangentialLocation": 6,
                "Temperature": 80.45579614256368
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_16_7",
                "RadialLocation": 16,
                "TangentialLocation": 7,
                "Temperature": 78.88415440920174
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_16_8",
                "RadialLocation": 16,
                "TangentialLocation": 8,
                "Temperature": 76.67997485792552
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 79.36710823976726
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_17_1",
                "RadialLocation": 17,
                "TangentialLocation": 1,
                "Temperature": 80.12134308053045
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_17_2",
                "RadialLocation": 17,
                "TangentialLocation": 2,
                "Temperature": 80.77859882937994
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_17_3",
                "RadialLocation": 17,
                "TangentialLocation": 3,
                "Temperature": 81.11826628653388
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_17_4",
                "RadialLocation": 17,
                "TangentialLocation": 4,
                "Temperature": 81.05978308705046
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_17_5",
                "RadialLocation": 17,
                "TangentialLocation": 5,
                "Temperature": 80.56841290752635
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_17_6",
                "RadialLocation": 17,
                "TangentialLocation": 6,
                "Temperature": 79.61736063026619
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_17_7",
                "RadialLocation": 17,
                "TangentialLocation": 7,
                "Temperature": 78.16864713753044
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_17_8",
                "RadialLocation": 17,
                "TangentialLocation": 8,
                "Temperature": 76.1630403972278
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 78.83554712240445
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_18_1",
                "RadialLocation": 18,
                "TangentialLocation": 1,
                "Temperature": 79.43440526653721
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_18_2",
                "RadialLocation": 18,
                "TangentialLocation": 2,
                "Temperature": 80.00674575546833
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_18_3",
                "RadialLocation": 18,
                "TangentialLocation": 3,
                "Temperature": 80.30558921930647
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_18_4",
                "RadialLocation": 18,
                "TangentialLocation": 4,
                "Temperature": 80.24020888003751
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_18_5",
                "RadialLocation": 18,
                "TangentialLocation": 5,
                "Temperature": 79.77295910062386
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_18_6",
                "RadialLocation": 18,
                "TangentialLocation": 6,
                "Temperature": 78.87911668886892
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_18_7",
                "RadialLocation": 18,
                "TangentialLocation": 7,
                "Temperature": 77.52989282234869
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "RotorWinding-Leading_Core_3_18_8",
                "RadialLocation": 18,
                "TangentialLocation": 8,
                "Temperature": 75.69185413315881
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 79.38151929198915
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_0_1",
                "RadialLocation": 0,
                "TangentialLocation": 1,
                "Temperature": 79.52895541817841
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_0_2",
                "RadialLocation": 0,
                "TangentialLocation": 2,
                "Temperature": 79.77879215819699
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_0_3",
                "RadialLocation": 0,
                "TangentialLocation": 3,
                "Temperature": 79.92333049742017
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_0_4",
                "RadialLocation": 0,
                "TangentialLocation": 4,
                "Temperature": 79.88742745920652
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_0_5",
                "RadialLocation": 0,
                "TangentialLocation": 5,
                "Temperature": 79.64026398506263
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_0_6",
                "RadialLocation": 0,
                "TangentialLocation": 6,
                "Temperature": 79.1610222009583
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_0_7",
                "RadialLocation": 0,
                "TangentialLocation": 7,
                "Temperature": 78.42964107052057
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_0_8",
                "RadialLocation": 0,
                "TangentialLocation": 8,
                "Temperature": 77.44922322129473
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 80.05202752895042
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_1_1",
                "RadialLocation": 1,
                "TangentialLocation": 1,
                "Temperature": 80.41594041673476
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_1_2",
                "RadialLocation": 1,
                "TangentialLocation": 2,
                "Temperature": 80.81235775447291
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_1_3",
                "RadialLocation": 1,
                "TangentialLocation": 3,
                "Temperature": 81.02940670611963
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_1_4",
                "RadialLocation": 1,
                "TangentialLocation": 4,
                "Temperature": 80.98263239621984
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_1_5",
                "RadialLocation": 1,
                "TangentialLocation": 5,
                "Temperature": 80.63569306195156
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_1_6",
                "RadialLocation": 1,
                "TangentialLocation": 6,
                "Temperature": 79.96639896115352
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_1_7",
                "RadialLocation": 1,
                "TangentialLocation": 7,
                "Temperature": 78.9629962356036
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_1_8",
                "RadialLocation": 1,
                "TangentialLocation": 8,
                "Temperature": 77.67458216397789
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 80.67724720139813
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_2_1",
                "RadialLocation": 2,
                "TangentialLocation": 1,
                "Temperature": 81.25882549553654
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_2_2",
                "RadialLocation": 2,
                "TangentialLocation": 2,
                "Temperature": 81.79060755738212
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_2_3",
                "RadialLocation": 2,
                "TangentialLocation": 3,
                "Temperature": 82.07308133472837
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_2_4",
                "RadialLocation": 2,
                "TangentialLocation": 4,
                "Temperature": 82.02435735420634
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_2_5",
                "RadialLocation": 2,
                "TangentialLocation": 5,
                "Temperature": 81.60882769221499
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_2_6",
                "RadialLocation": 2,
                "TangentialLocation": 6,
                "Temperature": 80.80652292692625
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_2_7",
                "RadialLocation": 2,
                "TangentialLocation": 7,
                "Temperature": 79.6119415557371
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_2_8",
                "RadialLocation": 2,
                "TangentialLocation": 8,
                "Temperature": 78.08784970130415
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 81.1889924161484
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_3_1",
                "RadialLocation": 3,
                "TangentialLocation": 1,
                "Temperature": 81.95526726705347
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_3_2",
                "RadialLocation": 3,
                "TangentialLocation": 2,
                "Temperature": 82.60268242761332
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_3_3",
                "RadialLocation": 3,
                "TangentialLocation": 3,
                "Temperature": 82.94250759381255
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_3_4",
                "RadialLocation": 3,
                "TangentialLocation": 4,
                "Temperature": 82.89727213133156
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_3_5",
                "RadialLocation": 3,
                "TangentialLocation": 5,
                "Temperature": 82.433714479429
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_3_6",
                "RadialLocation": 3,
                "TangentialLocation": 6,
                "Temperature": 81.53425551397656
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_3_7",
                "RadialLocation": 3,
                "TangentialLocation": 7,
                "Temperature": 80.19589249821361
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_3_8",
                "RadialLocation": 3,
                "TangentialLocation": 8,
                "Temperature": 78.48113378934673
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 81.58510718633909
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_4_1",
                "RadialLocation": 4,
                "TangentialLocation": 1,
                "Temperature": 82.49773156969523
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_4_2",
                "RadialLocation": 4,
                "TangentialLocation": 2,
                "Temperature": 83.23857669555704
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_4_3",
                "RadialLocation": 4,
                "TangentialLocation": 3,
                "Temperature": 83.62626750100009
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_4_4",
                "RadialLocation": 4,
                "TangentialLocation": 4,
                "Temperature": 83.5868632570999
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_4_5",
                "RadialLocation": 4,
                "TangentialLocation": 5,
                "Temperature": 83.08922561799672
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_4_6",
                "RadialLocation": 4,
                "TangentialLocation": 6,
                "Temperature": 82.11753661323661
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_4_7",
                "RadialLocation": 4,
                "TangentialLocation": 7,
                "Temperature": 80.66945365263564
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_4_8",
                "RadialLocation": 4,
                "TangentialLocation": 8,
                "Temperature": 78.80401187603748
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 81.88161511429652
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_5_1",
                "RadialLocation": 5,
                "TangentialLocation": 1,
                "Temperature": 82.90552000559775
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_5_2",
                "RadialLocation": 5,
                "TangentialLocation": 2,
                "Temperature": 83.71865421733341
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_5_3",
                "RadialLocation": 5,
                "TangentialLocation": 3,
                "Temperature": 84.1443994312884
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_5_4",
                "RadialLocation": 5,
                "TangentialLocation": 4,
                "Temperature": 84.11116840019862
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_5_5",
                "RadialLocation": 5,
                "TangentialLocation": 5,
                "Temperature": 83.58932202933346
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_5_6",
                "RadialLocation": 5,
                "TangentialLocation": 6,
                "Temperature": 82.56420414418736
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_5_7",
                "RadialLocation": 5,
                "TangentialLocation": 7,
                "Temperature": 81.03350097751746
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_5_8",
                "RadialLocation": 5,
                "TangentialLocation": 8,
                "Temperature": 79.05289131923078
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 82.09598026808915
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_6_1",
                "RadialLocation": 6,
                "TangentialLocation": 1,
                "Temperature": 83.20117380329233
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_6_2",
                "RadialLocation": 6,
                "TangentialLocation": 2,
                "Temperature": 84.06779745397586
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_6_3",
                "RadialLocation": 6,
                "TangentialLocation": 3,
                "Temperature": 84.52226666687201
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_6_4",
                "RadialLocation": 6,
                "TangentialLocation": 4,
                "Temperature": 84.49445322297873
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_6_5",
                "RadialLocation": 6,
                "TangentialLocation": 5,
                "Temperature": 83.9556715449359
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_6_6",
                "RadialLocation": 6,
                "TangentialLocation": 6,
                "Temperature": 82.89200131386144
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_6_7",
                "RadialLocation": 6,
                "TangentialLocation": 7,
                "Temperature": 81.30100885137826
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_6_8",
                "RadialLocation": 6,
                "TangentialLocation": 8,
                "Temperature": 79.2358325968749
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 82.24237977265744
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_7_1",
                "RadialLocation": 7,
                "TangentialLocation": 1,
                "Temperature": 83.40345318664409
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_7_2",
                "RadialLocation": 7,
                "TangentialLocation": 2,
                "Temperature": 84.30715989991607
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_7_3",
                "RadialLocation": 7,
                "TangentialLocation": 3,
                "Temperature": 84.78180158671134
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_7_4",
                "RadialLocation": 7,
                "TangentialLocation": 4,
                "Temperature": 84.75811377603785
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_7_5",
                "RadialLocation": 7,
                "TangentialLocation": 5,
                "Temperature": 84.20798307904838
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_7_6",
                "RadialLocation": 7,
                "TangentialLocation": 6,
                "Temperature": 83.11794590824671
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_7_7",
                "RadialLocation": 7,
                "TangentialLocation": 7,
                "Temperature": 81.48545894756394
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_7_8",
                "RadialLocation": 7,
                "TangentialLocation": 8,
                "Temperature": 79.36194166254226
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 82.33087552777567
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_8_1",
                "RadialLocation": 8,
                "TangentialLocation": 1,
                "Temperature": 83.52584919050618
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_8_2",
                "RadialLocation": 8,
                "TangentialLocation": 2,
                "Temperature": 84.45214919546765
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_8_3",
                "RadialLocation": 8,
                "TangentialLocation": 3,
                "Temperature": 84.93914732215157
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_8_4",
                "RadialLocation": 8,
                "TangentialLocation": 4,
                "Temperature": 84.91805261493191
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_8_5",
                "RadialLocation": 8,
                "TangentialLocation": 5,
                "Temperature": 84.3610765390384
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_8_6",
                "RadialLocation": 8,
                "TangentialLocation": 6,
                "Temperature": 83.25503360112803
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_8_7",
                "RadialLocation": 8,
                "TangentialLocation": 7,
                "Temperature": 81.59733189596164
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_8_8",
                "RadialLocation": 8,
                "TangentialLocation": 8,
                "Temperature": 79.43838660461248
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 82.36763257078272
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_9_1",
                "RadialLocation": 9,
                "TangentialLocation": 1,
                "Temperature": 83.57669013684823
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_9_2",
                "RadialLocation": 9,
                "TangentialLocation": 2,
                "Temperature": 84.51234823995514
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_9_3",
                "RadialLocation": 9,
                "TangentialLocation": 3,
                "Temperature": 85.00440155929014
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_9_4",
                "RadialLocation": 9,
                "TangentialLocation": 4,
                "Temperature": 84.98425658450455
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_9_5",
                "RadialLocation": 9,
                "TangentialLocation": 5,
                "Temperature": 84.42428722903098
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_9_6",
                "RadialLocation": 9,
                "TangentialLocation": 6,
                "Temperature": 83.31147305392852
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_9_7",
                "RadialLocation": 9,
                "TangentialLocation": 7,
                "Temperature": 81.64326076882328
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_9_8",
                "RadialLocation": 9,
                "TangentialLocation": 8,
                "Temperature": 79.46970193927226
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 82.35526260458184
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_10_1",
                "RadialLocation": 10,
                "TangentialLocation": 1,
                "Temperature": 83.55952228875638
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_10_2",
                "RadialLocation": 10,
                "TangentialLocation": 2,
                "Temperature": 84.49185237277032
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_10_3",
                "RadialLocation": 10,
                "TangentialLocation": 3,
                "Temperature": 84.98187710275324
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_10_4",
                "RadialLocation": 10,
                "TangentialLocation": 4,
                "Temperature": 84.96096520572551
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_10_5",
                "RadialLocation": 10,
                "TangentialLocation": 5,
                "Temperature": 84.40153218282686
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_10_6",
                "RadialLocation": 10,
                "TangentialLocation": 6,
                "Temperature": 83.2906541854856
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_10_7",
                "RadialLocation": 10,
                "TangentialLocation": 7,
                "Temperature": 81.62593735619204
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_10_8",
                "RadialLocation": 10,
                "TangentialLocation": 8,
                "Temperature": 79.45770111704078
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 82.29302870153218
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_11_1",
                "RadialLocation": 11,
                "TangentialLocation": 1,
                "Temperature": 83.47336651571878
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_11_2",
                "RadialLocation": 11,
                "TangentialLocation": 2,
                "Temperature": 84.38953730283406
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_11_3",
                "RadialLocation": 11,
                "TangentialLocation": 3,
                "Temperature": 84.87035164252863
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_11_4",
                "RadialLocation": 11,
                "TangentialLocation": 4,
                "Temperature": 84.84687764562075
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_11_5",
                "RadialLocation": 11,
                "TangentialLocation": 5,
                "Temperature": 84.29145494415452
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_11_6",
                "RadialLocation": 11,
                "TangentialLocation": 6,
                "Temperature": 83.19122389165804
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_11_7",
                "RadialLocation": 11,
                "TangentialLocation": 7,
                "Temperature": 81.54413270111152
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_11_8",
                "RadialLocation": 11,
                "TangentialLocation": 8,
                "Temperature": 79.40147351868194
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 82.17687999216844
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_12_1",
                "RadialLocation": 12,
                "TangentialLocation": 1,
                "Temperature": 83.31279941021572
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_12_2",
                "RadialLocation": 12,
                "TangentialLocation": 2,
                "Temperature": 84.1991917227936
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_12_3",
                "RadialLocation": 12,
                "TangentialLocation": 3,
                "Temperature": 84.66323156598756
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_12_4",
                "RadialLocation": 12,
                "TangentialLocation": 4,
                "Temperature": 84.63531132780875
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_12_5",
                "RadialLocation": 12,
                "TangentialLocation": 5,
                "Temperature": 84.08754016281551
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_12_6",
                "RadialLocation": 12,
                "TangentialLocation": 6,
                "Temperature": 83.00713088488394
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_12_7",
                "RadialLocation": 12,
                "TangentialLocation": 7,
                "Temperature": 81.39267411177359
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_12_8",
                "RadialLocation": 12,
                "TangentialLocation": 8,
                "Temperature": 79.29733136095594
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 81.99943903605636
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_13_1",
                "RadialLocation": 13,
                "TangentialLocation": 1,
                "Temperature": 83.06804604728515
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_13_2",
                "RadialLocation": 13,
                "TangentialLocation": 2,
                "Temperature": 83.90975306842464
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_13_3",
                "RadialLocation": 13,
                "TangentialLocation": 3,
                "Temperature": 84.34889718117503
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_13_4",
                "RadialLocation": 13,
                "TangentialLocation": 4,
                "Temperature": 84.31458200203372
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_13_5",
                "RadialLocation": 13,
                "TangentialLocation": 5,
                "Temperature": 83.77844275788141
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_13_6",
                "RadialLocation": 13,
                "TangentialLocation": 6,
                "Temperature": 82.7278342973806
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_13_7",
                "RadialLocation": 13,
                "TangentialLocation": 7,
                "Temperature": 81.16250760975919
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_13_8",
                "RadialLocation": 13,
                "TangentialLocation": 8,
                "Temperature": 79.13877280954374
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 81.75038669472293
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_14_1",
                "RadialLocation": 14,
                "TangentialLocation": 1,
                "Temperature": 82.72574249529679
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_14_2",
                "RadialLocation": 14,
                "TangentialLocation": 2,
                "Temperature": 83.50645873068717
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_14_3",
                "RadialLocation": 14,
                "TangentialLocation": 3,
                "Temperature": 83.91212468537128
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_14_4",
                "RadialLocation": 14,
                "TangentialLocation": 4,
                "Temperature": 83.86951738335178
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_14_5",
                "RadialLocation": 14,
                "TangentialLocation": 5,
                "Temperature": 83.34939980885363
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_14_6",
                "RadialLocation": 14,
                "TangentialLocation": 6,
                "Temperature": 82.33943913447324
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_14_7",
                "RadialLocation": 14,
                "TangentialLocation": 7,
                "Temperature": 80.84144106495869
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_14_8",
                "RadialLocation": 14,
                "TangentialLocation": 8,
                "Temperature": 78.91683792007254
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 81.41864437459392
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_15_1",
                "RadialLocation": 15,
                "TangentialLocation": 1,
                "Temperature": 82.27234278935124
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_15_2",
                "RadialLocation": 15,
                "TangentialLocation": 2,
                "Temperature": 82.97524561787142
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_15_3",
                "RadialLocation": 15,
                "TangentialLocation": 3,
                "Temperature": 83.33908692047333
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_15_4",
                "RadialLocation": 15,
                "TangentialLocation": 4,
                "Temperature": 83.28663340981734
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_15_5",
                "RadialLocation": 15,
                "TangentialLocation": 5,
                "Temperature": 82.7871631219569
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_15_6",
                "RadialLocation": 15,
                "TangentialLocation": 6,
                "Temperature": 81.82897577102042
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_15_7",
                "RadialLocation": 15,
                "TangentialLocation": 7,
                "Temperature": 80.41739388622324
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_15_8",
                "RadialLocation": 15,
                "TangentialLocation": 8,
                "Temperature": 78.62208640237193
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 81.00058614887018
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_16_1",
                "RadialLocation": 16,
                "TangentialLocation": 1,
                "Temperature": 81.70585590930965
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_16_2",
                "RadialLocation": 16,
                "TangentialLocation": 2,
                "Temperature": 82.31683341481575
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_16_3",
                "RadialLocation": 16,
                "TangentialLocation": 3,
                "Temperature": 82.63265929339865
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_16_4",
                "RadialLocation": 16,
                "TangentialLocation": 4,
                "Temperature": 82.56971206770856
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_16_5",
                "RadialLocation": 16,
                "TangentialLocation": 5,
                "Temperature": 82.0949938545339
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_16_6",
                "RadialLocation": 16,
                "TangentialLocation": 6,
                "Temperature": 81.1979164817752
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_16_7",
                "RadialLocation": 16,
                "TangentialLocation": 7,
                "Temperature": 79.8893881278558
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_16_8",
                "RadialLocation": 16,
                "TangentialLocation": 8,
                "Temperature": 78.25191083604979
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 80.52620807207677
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_17_1",
                "RadialLocation": 17,
                "TangentialLocation": 1,
                "Temperature": 81.07108532273902
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_17_2",
                "RadialLocation": 17,
                "TangentialLocation": 2,
                "Temperature": 81.58696536341726
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_17_3",
                "RadialLocation": 17,
                "TangentialLocation": 3,
                "Temperature": 81.8548779345925
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_17_4",
                "RadialLocation": 17,
                "TangentialLocation": 4,
                "Temperature": 81.78254089998866
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_17_5",
                "RadialLocation": 17,
                "TangentialLocation": 5,
                "Temperature": 81.33406002077247
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_17_6",
                "RadialLocation": 17,
                "TangentialLocation": 6,
                "Temperature": 80.50042904452168
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_17_7",
                "RadialLocation": 17,
                "TangentialLocation": 7,
                "Temperature": 79.30011599806168
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_17_8",
                "RadialLocation": 17,
                "TangentialLocation": 8,
                "Temperature": 77.83356068386598
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 80.12842159058378
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_18_1",
                "RadialLocation": 18,
                "TangentialLocation": 1,
                "Temperature": 80.54774886228472
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_18_2",
                "RadialLocation": 18,
                "TangentialLocation": 2,
                "Temperature": 80.99295422143823
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_18_3",
                "RadialLocation": 18,
                "TangentialLocation": 3,
                "Temperature": 81.22660999036256
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_18_4",
                "RadialLocation": 18,
                "TangentialLocation": 4,
                "Temperature": 81.14850345787566
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_18_5",
                "RadialLocation": 18,
                "TangentialLocation": 5,
                "Temperature": 80.72030393304097
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_18_6",
                "RadialLocation": 18,
                "TangentialLocation": 6,
                "Temperature": 79.93448179986778
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_18_7",
                "RadialLocation": 18,
                "TangentialLocation": 7,
                "Temperature": 78.81643329586096
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "RotorWinding-Leading_Core_4_18_8",
                "RadialLocation": 18,
                "TangentialLocation": 8,
                "Temperature": 77.48438340353957
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 80.65123628889121
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_0_1",
                "RadialLocation": 0,
                "TangentialLocation": 1,
                "Temperature": 80.69443872027597
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_0_2",
                "RadialLocation": 0,
                "TangentialLocation": 2,
                "Temperature": 80.86173153776
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_0_3",
                "RadialLocation": 0,
                "TangentialLocation": 3,
                "Temperature": 80.96214338911135
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_0_4",
                "RadialLocation": 0,
                "TangentialLocation": 4,
                "Temperature": 80.91866230211762
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_0_5",
                "RadialLocation": 0,
                "TangentialLocation": 5,
                "Temperature": 80.7019576923881
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_0_6",
                "RadialLocation": 0,
                "TangentialLocation": 6,
                "Temperature": 80.30506067786324
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_0_7",
                "RadialLocation": 0,
                "TangentialLocation": 7,
                "Temperature": 79.75037003815171
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_0_8",
                "RadialLocation": 0,
                "TangentialLocation": 8,
                "Temperature": 79.15821340766203
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 81.12266602669912
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_1_1",
                "RadialLocation": 1,
                "TangentialLocation": 1,
                "Temperature": 81.32998026204314
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_1_2",
                "RadialLocation": 1,
                "TangentialLocation": 2,
                "Temperature": 81.6143412686766
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_1_3",
                "RadialLocation": 1,
                "TangentialLocation": 3,
                "Temperature": 81.77263294706098
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_1_4",
                "RadialLocation": 1,
                "TangentialLocation": 4,
                "Temperature": 81.7157055272727
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_1_5",
                "RadialLocation": 1,
                "TangentialLocation": 5,
                "Temperature": 81.40865948537233
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_1_6",
                "RadialLocation": 1,
                "TangentialLocation": 6,
                "Temperature": 80.84634279909224
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_1_7",
                "RadialLocation": 1,
                "TangentialLocation": 7,
                "Temperature": 80.06737901798792
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_1_8",
                "RadialLocation": 1,
                "TangentialLocation": 8,
                "Temperature": 79.24924136125392
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 81.62963041557556
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_2_1",
                "RadialLocation": 2,
                "TangentialLocation": 1,
                "Temperature": 82.02119627627752
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_2_2",
                "RadialLocation": 2,
                "TangentialLocation": 2,
                "Temperature": 82.42281671236371
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_2_3",
                "RadialLocation": 2,
                "TangentialLocation": 3,
                "Temperature": 82.63769296638182
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_2_4",
                "RadialLocation": 2,
                "TangentialLocation": 4,
                "Temperature": 82.5771290289967
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_2_5",
                "RadialLocation": 2,
                "TangentialLocation": 5,
                "Temperature": 82.20665558517061
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_2_6",
                "RadialLocation": 2,
                "TangentialLocation": 6,
                "Temperature": 81.5244762613025
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_2_7",
                "RadialLocation": 2,
                "TangentialLocation": 7,
                "Temperature": 80.57832398378314
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_2_8",
                "RadialLocation": 2,
                "TangentialLocation": 8,
                "Temperature": 79.5644510319412
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 82.07248002887985
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_3_1",
                "RadialLocation": 3,
                "TangentialLocation": 1,
                "Temperature": 82.6285971955612
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_3_2",
                "RadialLocation": 3,
                "TangentialLocation": 2,
                "Temperature": 83.13472775714351
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_3_3",
                "RadialLocation": 3,
                "TangentialLocation": 3,
                "Temperature": 83.40142763609414
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_3_4",
                "RadialLocation": 3,
                "TangentialLocation": 4,
                "Temperature": 83.34319979692343
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_3_5",
                "RadialLocation": 3,
                "TangentialLocation": 5,
                "Temperature": 82.9276672432004
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_3_6",
                "RadialLocation": 3,
                "TangentialLocation": 6,
                "Temperature": 82.1558385303651
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_3_7",
                "RadialLocation": 3,
                "TangentialLocation": 7,
                "Temperature": 81.07921376719706
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_3_8",
                "RadialLocation": 3,
                "TangentialLocation": 8,
                "Temperature": 79.8969497788575
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 82.42869277144908
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_4_1",
                "RadialLocation": 4,
                "TangentialLocation": 1,
                "Temperature": 83.11923813302172
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_4_2",
                "RadialLocation": 4,
                "TangentialLocation": 2,
                "Temperature": 83.71204718600696
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_4_3",
                "RadialLocation": 4,
                "TangentialLocation": 3,
                "Temperature": 84.02317505996838
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_4_4",
                "RadialLocation": 4,
                "TangentialLocation": 4,
                "Temperature": 83.9700075815612
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_4_5",
                "RadialLocation": 4,
                "TangentialLocation": 5,
                "Temperature": 83.5221335593685
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_4_6",
                "RadialLocation": 4,
                "TangentialLocation": 6,
                "Temperature": 82.68248271778235
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_4_7",
                "RadialLocation": 4,
                "TangentialLocation": 7,
                "Temperature": 81.50384445430906
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_4_8",
                "RadialLocation": 4,
                "TangentialLocation": 8,
                "Temperature": 80.18379439717192
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 82.7021680888662
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_5_1",
                "RadialLocation": 5,
                "TangentialLocation": 1,
                "Temperature": 83.4970141263885
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_5_2",
                "RadialLocation": 5,
                "TangentialLocation": 2,
                "Temperature": 84.1580759952215
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_5_3",
                "RadialLocation": 5,
                "TangentialLocation": 3,
                "Temperature": 84.50515863364915
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_5_4",
                "RadialLocation": 5,
                "TangentialLocation": 4,
                "Temperature": 84.45766648498913
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_5_5",
                "RadialLocation": 5,
                "TangentialLocation": 5,
                "Temperature": 83.98660084605375
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_5_6",
                "RadialLocation": 5,
                "TangentialLocation": 6,
                "Temperature": 83.0961185625792
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_5_7",
                "RadialLocation": 5,
                "TangentialLocation": 7,
                "Temperature": 81.83936380168504
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_5_8",
                "RadialLocation": 5,
                "TangentialLocation": 8,
                "Temperature": 80.41164958298009
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 82.903346234522
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_6_1",
                "RadialLocation": 6,
                "TangentialLocation": 1,
                "Temperature": 83.77544674628771
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_6_2",
                "RadialLocation": 6,
                "TangentialLocation": 2,
                "Temperature": 84.48762932250034
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_6_3",
                "RadialLocation": 6,
                "TangentialLocation": 3,
                "Temperature": 84.86218309514517
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_6_4",
                "RadialLocation": 6,
                "TangentialLocation": 4,
                "Temperature": 84.81979876777798
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_6_5",
                "RadialLocation": 6,
                "TangentialLocation": 5,
                "Temperature": 84.33238584402343
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_6_6",
                "RadialLocation": 6,
                "TangentialLocation": 6,
                "Temperature": 83.40486512855466
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_6_7",
                "RadialLocation": 6,
                "TangentialLocation": 7,
                "Temperature": 82.09043265140465
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_6_8",
                "RadialLocation": 6,
                "TangentialLocation": 8,
                "Temperature": 80.5824812944496
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 83.04239375206798
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_7_1",
                "RadialLocation": 7,
                "TangentialLocation": 1,
                "Temperature": 83.96811102654459
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_7_2",
                "RadialLocation": 7,
                "TangentialLocation": 2,
                "Temperature": 84.71603382032274
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_7_3",
                "RadialLocation": 7,
                "TangentialLocation": 3,
                "Temperature": 85.1100413110914
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_7_4",
                "RadialLocation": 7,
                "TangentialLocation": 4,
                "Temperature": 85.0715996083726
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_7_5",
                "RadialLocation": 7,
                "TangentialLocation": 5,
                "Temperature": 84.57316755804622
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_7_6",
                "RadialLocation": 7,
                "TangentialLocation": 6,
                "Temperature": 83.6201351990488
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_7_7",
                "RadialLocation": 7,
                "TangentialLocation": 7,
                "Temperature": 82.26567883118865
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_7_8",
                "RadialLocation": 7,
                "TangentialLocation": 8,
                "Temperature": 80.70181434228128
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 83.12714455961233
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_8_1",
                "RadialLocation": 8,
                "TangentialLocation": 1,
                "Temperature": 84.08560488916238
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_8_2",
                "RadialLocation": 8,
                "TangentialLocation": 2,
                "Temperature": 84.85542985666652
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_8_3",
                "RadialLocation": 8,
                "TangentialLocation": 3,
                "Temperature": 85.26142122116744
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_8_4",
                "RadialLocation": 8,
                "TangentialLocation": 4,
                "Temperature": 85.22547636592263
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_8_5",
                "RadialLocation": 8,
                "TangentialLocation": 5,
                "Temperature": 84.72036823288157
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_8_6",
                "RadialLocation": 8,
                "TangentialLocation": 6,
                "Temperature": 83.75177019183957
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_8_7",
                "RadialLocation": 8,
                "TangentialLocation": 7,
                "Temperature": 82.37285351509891
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_8_8",
                "RadialLocation": 8,
                "TangentialLocation": 8,
                "Temperature": 80.77480218173358
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 83.16263190284938
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_9_1",
                "RadialLocation": 9,
                "TangentialLocation": 1,
                "Temperature": 84.13478299805153
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_9_2",
                "RadialLocation": 9,
                "TangentialLocation": 2,
                "Temperature": 84.91373067820663
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_9_3",
                "RadialLocation": 9,
                "TangentialLocation": 3,
                "Temperature": 85.32465049363218
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_9_4",
                "RadialLocation": 9,
                "TangentialLocation": 4,
                "Temperature": 85.28962361985309
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_9_5",
                "RadialLocation": 9,
                "TangentialLocation": 5,
                "Temperature": 84.78158179803792
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_9_6",
                "RadialLocation": 9,
                "TangentialLocation": 6,
                "Temperature": 83.80636446100657
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_9_7",
                "RadialLocation": 9,
                "TangentialLocation": 7,
                "Temperature": 82.41719497748012
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_9_8",
                "RadialLocation": 9,
                "TangentialLocation": 8,
                "Temperature": 80.80495076090632
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 83.15108396526378
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_10_1",
                "RadialLocation": 10,
                "TangentialLocation": 1,
                "Temperature": 84.1186912797101
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_10_2",
                "RadialLocation": 10,
                "TangentialLocation": 2,
                "Temperature": 84.8944634931652
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_10_3",
                "RadialLocation": 10,
                "TangentialLocation": 3,
                "Temperature": 85.30343887989946
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_10_4",
                "RadialLocation": 10,
                "TangentialLocation": 4,
                "Temperature": 85.26767048200537
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_10_5",
                "RadialLocation": 10,
                "TangentialLocation": 5,
                "Temperature": 84.76013348030168
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_10_6",
                "RadialLocation": 10,
                "TangentialLocation": 6,
                "Temperature": 83.78676118611416
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_10_7",
                "RadialLocation": 10,
                "TangentialLocation": 7,
                "Temperature": 82.40092437298456
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_10_8",
                "RadialLocation": 10,
                "TangentialLocation": 8,
                "Temperature": 80.79372742430196
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 83.09201028664724
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_11_1",
                "RadialLocation": 11,
                "TangentialLocation": 1,
                "Temperature": 84.03667084079798
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_11_2",
                "RadialLocation": 11,
                "TangentialLocation": 2,
                "Temperature": 84.79686624243705
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_11_3",
                "RadialLocation": 11,
                "TangentialLocation": 3,
                "Temperature": 85.19694832043841
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_11_4",
                "RadialLocation": 11,
                "TangentialLocation": 4,
                "Temperature": 85.15870683999476
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_11_5",
                "RadialLocation": 11,
                "TangentialLocation": 5,
                "Temperature": 84.65504958270179
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_11_6",
                "RadialLocation": 11,
                "TangentialLocation": 6,
                "Temperature": 83.69196618175259
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_11_7",
                "RadialLocation": 11,
                "TangentialLocation": 7,
                "Temperature": 82.32312672329213
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_11_8",
                "RadialLocation": 11,
                "TangentialLocation": 8,
                "Temperature": 80.74045529498642
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 82.98230861369944
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_12_1",
                "RadialLocation": 12,
                "TangentialLocation": 1,
                "Temperature": 83.8845304754849
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_12_2",
                "RadialLocation": 12,
                "TangentialLocation": 2,
                "Temperature": 84.61612052381369
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_12_3",
                "RadialLocation": 12,
                "TangentialLocation": 3,
                "Temperature": 85.00006078642981
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_12_4",
                "RadialLocation": 12,
                "TangentialLocation": 4,
                "Temperature": 84.957546948936
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_12_5",
                "RadialLocation": 12,
                "TangentialLocation": 5,
                "Temperature": 84.46127595210586
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_12_6",
                "RadialLocation": 12,
                "TangentialLocation": 6,
                "Temperature": 83.51729259853413
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_12_7",
                "RadialLocation": 12,
                "TangentialLocation": 7,
                "Temperature": 82.17981815824385
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_12_8",
                "RadialLocation": 12,
                "TangentialLocation": 8,
                "Temperature": 80.64232923290118
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 82.8165284949114
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_13_1",
                "RadialLocation": 13,
                "TangentialLocation": 1,
                "Temperature": 83.65498945386058
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_13_2",
                "RadialLocation": 13,
                "TangentialLocation": 2,
                "Temperature": 84.34397197029249
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_13_3",
                "RadialLocation": 13,
                "TangentialLocation": 3,
                "Temperature": 84.70412239130513
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_13_4",
                "RadialLocation": 13,
                "TangentialLocation": 4,
                "Temperature": 84.65551081662298
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_13_5",
                "RadialLocation": 13,
                "TangentialLocation": 5,
                "Temperature": 84.17040141185338
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_13_6",
                "RadialLocation": 13,
                "TangentialLocation": 6,
                "Temperature": 83.25494469528768
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_13_7",
                "RadialLocation": 13,
                "TangentialLocation": 7,
                "Temperature": 81.96434375888815
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_13_8",
                "RadialLocation": 13,
                "TangentialLocation": 8,
                "Temperature": 80.49463381283203
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 82.58778256354924
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_14_1",
                "RadialLocation": 14,
                "TangentialLocation": 1,
                "Temperature": 83.33909709440395
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_14_2",
                "RadialLocation": 14,
                "TangentialLocation": 2,
                "Temperature": 83.97059302783885
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_14_3",
                "RadialLocation": 14,
                "TangentialLocation": 3,
                "Temperature": 84.29909626723557
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_14_4",
                "RadialLocation": 14,
                "TangentialLocation": 4,
                "Temperature": 84.24267053690379
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_14_5",
                "RadialLocation": 14,
                "TangentialLocation": 5,
                "Temperature": 83.7727910666842
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_14_6",
                "RadialLocation": 14,
                "TangentialLocation": 6,
                "Temperature": 82.89584495701735
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_14_7",
                "RadialLocation": 14,
                "TangentialLocation": 7,
                "Temperature": 81.66874648354388
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_14_8",
                "RadialLocation": 14,
                "TangentialLocation": 8,
                "Temperature": 80.29158123452835
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 82.29068455432133
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_15_1",
                "RadialLocation": 15,
                "TangentialLocation": 1,
                "Temperature": 82.93054640534235
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_15_2",
                "RadialLocation": 15,
                "TangentialLocation": 2,
                "Temperature": 83.48992928928904
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_15_3",
                "RadialLocation": 15,
                "TangentialLocation": 3,
                "Temperature": 83.77951360934141
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_15_4",
                "RadialLocation": 15,
                "TangentialLocation": 4,
                "Temperature": 83.7139717901338
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_15_5",
                "RadialLocation": 15,
                "TangentialLocation": 5,
                "Temperature": 83.26345610433923
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_15_6",
                "RadialLocation": 15,
                "TangentialLocation": 6,
                "Temperature": 82.43483078979371
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_15_7",
                "RadialLocation": 15,
                "TangentialLocation": 7,
                "Temperature": 81.28787366339975
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_15_8",
                "RadialLocation": 15,
                "TangentialLocation": 8,
                "Temperature": 80.02897371208189
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 81.92991789824383
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_16_1",
                "RadialLocation": 16,
                "TangentialLocation": 1,
                "Temperature": 82.4376923901025
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_16_2",
                "RadialLocation": 16,
                "TangentialLocation": 2,
                "Temperature": 82.9139426212159
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_16_3",
                "RadialLocation": 16,
                "TangentialLocation": 3,
                "Temperature": 83.15985611549279
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_16_4",
                "RadialLocation": 16,
                "TangentialLocation": 4,
                "Temperature": 83.08486008561974
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_16_5",
                "RadialLocation": 16,
                "TangentialLocation": 5,
                "Temperature": 82.65712211669151
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_16_6",
                "RadialLocation": 16,
                "TangentialLocation": 6,
                "Temperature": 81.88431558643252
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_16_7",
                "RadialLocation": 16,
                "TangentialLocation": 7,
                "Temperature": 80.8306094574781
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_16_8",
                "RadialLocation": 16,
                "TangentialLocation": 8,
                "Temperature": 79.71181197410431
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 81.54253974040687
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_17_1",
                "RadialLocation": 17,
                "TangentialLocation": 1,
                "Temperature": 81.91352506321786
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_17_2",
                "RadialLocation": 17,
                "TangentialLocation": 2,
                "Temperature": 82.30677939931287
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_17_3",
                "RadialLocation": 17,
                "TangentialLocation": 3,
                "Temperature": 82.51055175236904
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_17_4",
                "RadialLocation": 17,
                "TangentialLocation": 4,
                "Temperature": 82.42746715812413
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_17_5",
                "RadialLocation": 17,
                "TangentialLocation": 5,
                "Temperature": 82.02324119783744
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_17_6",
                "RadialLocation": 17,
                "TangentialLocation": 6,
                "Temperature": 81.30660968796718
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_17_7",
                "RadialLocation": 17,
                "TangentialLocation": 7,
                "Temperature": 80.34735612980009
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_17_8",
                "RadialLocation": 17,
                "TangentialLocation": 8,
                "Temperature": 79.37369461378943
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 81.24314608847665
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_18_1",
                "RadialLocation": 18,
                "TangentialLocation": 1,
                "Temperature": 81.51339165711926
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_18_2",
                "RadialLocation": 18,
                "TangentialLocation": 2,
                "Temperature": 81.84801822952232
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_18_3",
                "RadialLocation": 18,
                "TangentialLocation": 3,
                "Temperature": 82.02309631185187
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_18_4",
                "RadialLocation": 18,
                "TangentialLocation": 4,
                "Temperature": 81.9354181558852
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_18_5",
                "RadialLocation": 18,
                "TangentialLocation": 5,
                "Temperature": 81.54871739422873
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_18_6",
                "RadialLocation": 18,
                "TangentialLocation": 6,
                "Temperature": 80.87258191332148
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_18_7",
                "RadialLocation": 18,
                "TangentialLocation": 7,
                "Temperature": 79.98148473131668
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "RotorWinding-Leading_Core_5_18_8",
                "RadialLocation": 18,
                "TangentialLocation": 8,
                "Temperature": 79.11488513157705
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 81.74533440080106
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_0_1",
                "RadialLocation": 0,
                "TangentialLocation": 1,
                "Temperature": 81.70987097372772
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_0_2",
                "RadialLocation": 0,
                "TangentialLocation": 2,
                "Temperature": 81.8110369407765
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_0_3",
                "RadialLocation": 0,
                "TangentialLocation": 3,
                "Temperature": 81.87465498804684
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_0_4",
                "RadialLocation": 0,
                "TangentialLocation": 4,
                "Temperature": 81.82539257804741
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_0_5",
                "RadialLocation": 0,
                "TangentialLocation": 5,
                "Temperature": 81.63684719759131
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_0_6",
                "RadialLocation": 0,
                "TangentialLocation": 6,
                "Temperature": 81.31473376920279
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_0_7",
                "RadialLocation": 0,
                "TangentialLocation": 7,
                "Temperature": 80.91710514769092
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_0_8",
                "RadialLocation": 0,
                "TangentialLocation": 8,
                "Temperature": 80.65784642105729
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 82.0484288237064
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_1_1",
                "RadialLocation": 1,
                "TangentialLocation": 1,
                "Temperature": 82.13138909120876
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_1_2",
                "RadialLocation": 1,
                "TangentialLocation": 2,
                "Temperature": 82.32300458606868
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_1_3",
                "RadialLocation": 1,
                "TangentialLocation": 3,
                "Temperature": 82.431132494416
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_1_4",
                "RadialLocation": 1,
                "TangentialLocation": 4,
                "Temperature": 82.36653500205095
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_1_5",
                "RadialLocation": 1,
                "TangentialLocation": 5,
                "Temperature": 82.09757400766168
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_1_6",
                "RadialLocation": 1,
                "TangentialLocation": 6,
                "Temperature": 81.63466897918559
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_1_7",
                "RadialLocation": 1,
                "TangentialLocation": 7,
                "Temperature": 81.05838192656834
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_1_8",
                "RadialLocation": 1,
                "TangentialLocation": 8,
                "Temperature": 80.64613949824098
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 82.45347523758458
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_2_1",
                "RadialLocation": 2,
                "TangentialLocation": 1,
                "Temperature": 82.68922306754315
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_2_2",
                "RadialLocation": 2,
                "TangentialLocation": 2,
                "Temperature": 82.98049671297264
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_2_3",
                "RadialLocation": 2,
                "TangentialLocation": 3,
                "Temperature": 83.13662174316894
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_2_4",
                "RadialLocation": 2,
                "TangentialLocation": 4,
                "Temperature": 83.06698764989086
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_2_5",
                "RadialLocation": 2,
                "TangentialLocation": 5,
                "Temperature": 82.74017269041006
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_2_6",
                "RadialLocation": 2,
                "TangentialLocation": 6,
                "Temperature": 82.17099663434749
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_2_7",
                "RadialLocation": 2,
                "TangentialLocation": 7,
                "Temperature": 81.45146384158616
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_2_8",
                "RadialLocation": 2,
                "TangentialLocation": 8,
                "Temperature": 80.880865604424
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 82.83584723849428
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_3_1",
                "RadialLocation": 3,
                "TangentialLocation": 1,
                "Temperature": 83.21610976200036
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_3_2",
                "RadialLocation": 3,
                "TangentialLocation": 2,
                "Temperature": 83.6005047726437
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_3_3",
                "RadialLocation": 3,
                "TangentialLocation": 3,
                "Temperature": 83.80284627456885
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_3_4",
                "RadialLocation": 3,
                "TangentialLocation": 4,
                "Temperature": 83.7344741803855
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_3_5",
                "RadialLocation": 3,
                "TangentialLocation": 5,
                "Temperature": 83.36578466236674
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_3_6",
                "RadialLocation": 3,
                "TangentialLocation": 6,
                "Temperature": 82.71482173806868
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_3_7",
                "RadialLocation": 3,
                "TangentialLocation": 7,
                "Temperature": 81.87855439724139
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_3_8",
                "RadialLocation": 3,
                "TangentialLocation": 8,
                "Temperature": 81.1614782083352
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 83.15685209626625
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_4_1",
                "RadialLocation": 4,
                "TangentialLocation": 1,
                "Temperature": 83.65913823357754
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_4_2",
                "RadialLocation": 4,
                "TangentialLocation": 2,
                "Temperature": 84.12298772599163
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_4_3",
                "RadialLocation": 4,
                "TangentialLocation": 3,
                "Temperature": 84.36613729289354
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_4_4",
                "RadialLocation": 4,
                "TangentialLocation": 4,
                "Temperature": 84.3020477840712
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_4_5",
                "RadialLocation": 4,
                "TangentialLocation": 5,
                "Temperature": 83.90287720254965
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_4_6",
                "RadialLocation": 4,
                "TangentialLocation": 6,
                "Temperature": 83.18879042671472
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_4_7",
                "RadialLocation": 4,
                "TangentialLocation": 7,
                "Temperature": 82.25875608248474
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_4_8",
                "RadialLocation": 4,
                "TangentialLocation": 8,
                "Temperature": 81.41718027931779
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 83.41015840482561
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_5_1",
                "RadialLocation": 5,
                "TangentialLocation": 1,
                "Temperature": 84.00917710318403
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_5_2",
                "RadialLocation": 5,
                "TangentialLocation": 2,
                "Temperature": 84.53677586353305
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_5_3",
                "RadialLocation": 5,
                "TangentialLocation": 3,
                "Temperature": 84.81358936111708
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_5_4",
                "RadialLocation": 5,
                "TangentialLocation": 4,
                "Temperature": 84.75464388054478
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_5_5",
                "RadialLocation": 5,
                "TangentialLocation": 5,
                "Temperature": 84.33337892569936
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_5_6",
                "RadialLocation": 5,
                "TangentialLocation": 6,
                "Temperature": 83.57129747277659
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_5_7",
                "RadialLocation": 5,
                "TangentialLocation": 7,
                "Temperature": 82.56816096874698
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_5_8",
                "RadialLocation": 5,
                "TangentialLocation": 8,
                "Temperature": 81.62699374850015
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 83.5999936112158
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_6_1",
                "RadialLocation": 6,
                "TangentialLocation": 1,
                "Temperature": 84.2717159403514
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_6_2",
                "RadialLocation": 6,
                "TangentialLocation": 2,
                "Temperature": 84.84768070805909
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_6_3",
                "RadialLocation": 6,
                "TangentialLocation": 3,
                "Temperature": 85.15055026832589
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_6_4",
                "RadialLocation": 6,
                "TangentialLocation": 4,
                "Temperature": 85.09636746731337
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_6_5",
                "RadialLocation": 6,
                "TangentialLocation": 5,
                "Temperature": 84.65940003910974
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_6_6",
                "RadialLocation": 6,
                "TangentialLocation": 6,
                "Temperature": 83.86198267004548
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_6_7",
                "RadialLocation": 6,
                "TangentialLocation": 7,
                "Temperature": 82.80420057370263
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_6_8",
                "RadialLocation": 6,
                "TangentialLocation": 8,
                "Temperature": 81.78765201077404
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 83.73287373148895
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_7_1",
                "RadialLocation": 7,
                "TangentialLocation": 1,
                "Temperature": 84.4555610586851
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_7_2",
                "RadialLocation": 7,
                "TangentialLocation": 2,
                "Temperature": 85.06564017503396
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_7_3",
                "RadialLocation": 7,
                "TangentialLocation": 3,
                "Temperature": 85.38712415227948
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_7_4",
                "RadialLocation": 7,
                "TangentialLocation": 4,
                "Temperature": 85.33667265742527
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_7_5",
                "RadialLocation": 7,
                "TangentialLocation": 5,
                "Temperature": 84.88905547530719
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_7_6",
                "RadialLocation": 7,
                "TangentialLocation": 6,
                "Temperature": 84.06711864000019
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_7_7",
                "RadialLocation": 7,
                "TangentialLocation": 7,
                "Temperature": 82.97109279408501
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_7_8",
                "RadialLocation": 7,
                "TangentialLocation": 8,
                "Temperature": 81.90146390388676
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 83.81457353710587
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_8_1",
                "RadialLocation": 8,
                "TangentialLocation": 1,
                "Temperature": 84.56859893192012
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_8_2",
                "RadialLocation": 8,
                "TangentialLocation": 2,
                "Temperature": 85.19971091375905
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_8_3",
                "RadialLocation": 8,
                "TangentialLocation": 3,
                "Temperature": 85.5327297696114
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_8_4",
                "RadialLocation": 8,
                "TangentialLocation": 4,
                "Temperature": 85.48466034487464
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_8_5",
                "RadialLocation": 8,
                "TangentialLocation": 5,
                "Temperature": 85.03056071229578
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_8_6",
                "RadialLocation": 8,
                "TangentialLocation": 6,
                "Temperature": 84.19358412280921
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_8_7",
                "RadialLocation": 8,
                "TangentialLocation": 7,
                "Temperature": 83.07404737254014
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_8_8",
                "RadialLocation": 8,
                "TangentialLocation": 8,
                "Temperature": 81.97173301140704
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 83.84907331564933
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_9_1",
                "RadialLocation": 9,
                "TangentialLocation": 1,
                "Temperature": 84.6162887441373
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_9_2",
                "RadialLocation": 9,
                "TangentialLocation": 2,
                "Temperature": 85.25621138390383
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_9_3",
                "RadialLocation": 9,
                "TangentialLocation": 3,
                "Temperature": 85.59399887121583
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_9_4",
                "RadialLocation": 9,
                "TangentialLocation": 4,
                "Temperature": 85.5468074533929
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_9_5",
                "RadialLocation": 9,
                "TangentialLocation": 5,
                "Temperature": 85.08984387340332
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_9_6",
                "RadialLocation": 9,
                "TangentialLocation": 6,
                "Temperature": 84.2464361391465
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_9_7",
                "RadialLocation": 9,
                "TangentialLocation": 7,
                "Temperature": 83.11698664730007
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_9_8",
                "RadialLocation": 9,
                "TangentialLocation": 8,
                "Temperature": 82.00101138259475
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 83.83824399804875
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_10_1",
                "RadialLocation": 10,
                "TangentialLocation": 1,
                "Temperature": 84.60119922599128
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_10_2",
                "RadialLocation": 10,
                "TangentialLocation": 2,
                "Temperature": 85.23812082413527
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_10_3",
                "RadialLocation": 10,
                "TangentialLocation": 3,
                "Temperature": 85.57405721089106
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_10_4",
                "RadialLocation": 10,
                "TangentialLocation": 4,
                "Temperature": 85.52615168702012
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_10_5",
                "RadialLocation": 10,
                "TangentialLocation": 5,
                "Temperature": 85.06965791200288
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_10_6",
                "RadialLocation": 10,
                "TangentialLocation": 6,
                "Temperature": 84.2279918093554
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_10_7",
                "RadialLocation": 10,
                "TangentialLocation": 7,
                "Temperature": 83.10168384123058
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_10_8",
                "RadialLocation": 10,
                "TangentialLocation": 8,
                "Temperature": 81.99044380975695
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 83.78182395962368
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_11_1",
                "RadialLocation": 11,
                "TangentialLocation": 1,
                "Temperature": 84.52297077866955
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_11_2",
                "RadialLocation": 11,
                "TangentialLocation": 2,
                "Temperature": 85.14501693056613
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_11_3",
                "RadialLocation": 11,
                "TangentialLocation": 3,
                "Temperature": 85.47242773010515
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_11_4",
                "RadialLocation": 11,
                "TangentialLocation": 4,
                "Temperature": 85.42215033726626
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_11_5",
                "RadialLocation": 11,
                "TangentialLocation": 5,
                "Temperature": 84.96938913240625
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_11_6",
                "RadialLocation": 11,
                "TangentialLocation": 6,
                "Temperature": 84.1375940228438
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_11_7",
                "RadialLocation": 11,
                "TangentialLocation": 7,
                "Temperature": 83.02751709290543
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_11_8",
                "RadialLocation": 11,
                "TangentialLocation": 8,
                "Temperature": 81.93956865965168
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 83.67758548883208
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_12_1",
                "RadialLocation": 12,
                "TangentialLocation": 1,
                "Temperature": 84.37856264601561
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_12_2",
                "RadialLocation": 12,
                "TangentialLocation": 2,
                "Temperature": 84.97339005608642
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_12_3",
                "RadialLocation": 12,
                "TangentialLocation": 3,
                "Temperature": 85.28538236918399
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_12_4",
                "RadialLocation": 12,
                "TangentialLocation": 4,
                "Temperature": 85.23102879513826
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_12_5",
                "RadialLocation": 12,
                "TangentialLocation": 5,
                "Temperature": 84.78536036815535
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_12_6",
                "RadialLocation": 12,
                "TangentialLocation": 6,
                "Temperature": 83.97183857325405
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_12_7",
                "RadialLocation": 12,
                "TangentialLocation": 7,
                "Temperature": 82.89161210852141
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_12_8",
                "RadialLocation": 12,
                "TangentialLocation": 8,
                "Temperature": 81.846392072854
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 83.52182881391798
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_13_1",
                "RadialLocation": 13,
                "TangentialLocation": 1,
                "Temperature": 84.16298554854185
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_13_2",
                "RadialLocation": 13,
                "TangentialLocation": 2,
                "Temperature": 84.71758031930253
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_13_3",
                "RadialLocation": 13,
                "TangentialLocation": 3,
                "Temperature": 85.00701365829956
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_13_4",
                "RadialLocation": 13,
                "TangentialLocation": 4,
                "Temperature": 84.94689142539048
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_13_5",
                "RadialLocation": 13,
                "TangentialLocation": 5,
                "Temperature": 84.5118791791702
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_13_6",
                "RadialLocation": 13,
                "TangentialLocation": 6,
                "Temperature": 83.7254688166775
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_13_7",
                "RadialLocation": 13,
                "TangentialLocation": 7,
                "Temperature": 82.68952012521436
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_13_8",
                "RadialLocation": 13,
                "TangentialLocation": 8,
                "Temperature": 81.70782081638838
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 83.31069924323852
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_14_1",
                "RadialLocation": 14,
                "TangentialLocation": 1,
                "Temperature": 83.87122077314253
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_14_2",
                "RadialLocation": 14,
                "TangentialLocation": 2,
                "Temperature": 84.37217512029241
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_14_3",
                "RadialLocation": 14,
                "TangentialLocation": 3,
                "Temperature": 84.63193315637884
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_14_4",
                "RadialLocation": 14,
                "TangentialLocation": 4,
                "Temperature": 84.56451440750989
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_14_5",
                "RadialLocation": 14,
                "TangentialLocation": 5,
                "Temperature": 84.14391225480662
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_14_6",
                "RadialLocation": 14,
                "TangentialLocation": 6,
                "Temperature": 83.3937273364223
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_14_7",
                "RadialLocation": 14,
                "TangentialLocation": 7,
                "Temperature": 82.41706869856579
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_14_8",
                "RadialLocation": 14,
                "TangentialLocation": 8,
                "Temperature": 81.5208780245301
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 83.04358925492079
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_15_1",
                "RadialLocation": 15,
                "TangentialLocation": 1,
                "Temperature": 83.50306228543081
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_15_2",
                "RadialLocation": 15,
                "TangentialLocation": 2,
                "Temperature": 83.9378806760705
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_15_3",
                "RadialLocation": 15,
                "TangentialLocation": 3,
                "Temperature": 84.1617330233464
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_15_4",
                "RadialLocation": 15,
                "TangentialLocation": 4,
                "Temperature": 84.08597187885151
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_15_5",
                "RadialLocation": 15,
                "TangentialLocation": 5,
                "Temperature": 83.68346608863531
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_15_6",
                "RadialLocation": 15,
                "TangentialLocation": 6,
                "Temperature": 82.97807442523397
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_15_7",
                "RadialLocation": 15,
                "TangentialLocation": 7,
                "Temperature": 82.07498390707656
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_15_8",
                "RadialLocation": 15,
                "TangentialLocation": 8,
                "Temperature": 81.28580272760331
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 82.73147177171921
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_16_1",
                "RadialLocation": 16,
                "TangentialLocation": 1,
                "Temperature": 83.07465755387298
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_16_2",
                "RadialLocation": 16,
                "TangentialLocation": 2,
                "Temperature": 83.43508647912729
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_16_3",
                "RadialLocation": 16,
                "TangentialLocation": 3,
                "Temperature": 83.61957524557324
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_16_4",
                "RadialLocation": 16,
                "TangentialLocation": 4,
                "Temperature": 83.535442741254
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_16_5",
                "RadialLocation": 16,
                "TangentialLocation": 5,
                "Temperature": 83.1538921609415
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_16_6",
                "RadialLocation": 16,
                "TangentialLocation": 6,
                "Temperature": 82.49922016680866
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_16_7",
                "RadialLocation": 16,
                "TangentialLocation": 7,
                "Temperature": 81.67969879779031
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_16_8",
                "RadialLocation": 16,
                "TangentialLocation": 8,
                "Temperature": 81.01347154481235
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 82.41494549957866
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_17_1",
                "RadialLocation": 17,
                "TangentialLocation": 1,
                "Temperature": 82.64270812464284
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_17_2",
                "RadialLocation": 17,
                "TangentialLocation": 2,
                "Temperature": 82.93140449090215
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_17_3",
                "RadialLocation": 17,
                "TangentialLocation": 3,
                "Temperature": 83.07915379563464
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_17_4",
                "RadialLocation": 17,
                "TangentialLocation": 4,
                "Temperature": 82.9882854390792
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_17_5",
                "RadialLocation": 17,
                "TangentialLocation": 5,
                "Temperature": 82.62799443425835
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_17_6",
                "RadialLocation": 17,
                "TangentialLocation": 6,
                "Temperature": 82.02306126222123
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_17_7",
                "RadialLocation": 17,
                "TangentialLocation": 7,
                "Temperature": 81.28539759905223
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_17_8",
                "RadialLocation": 17,
                "TangentialLocation": 8,
                "Temperature": 80.74095750101615
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 82.1904996696282
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_18_1",
                "RadialLocation": 18,
                "TangentialLocation": 1,
                "Temperature": 82.3381915986133
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_18_2",
                "RadialLocation": 18,
                "TangentialLocation": 2,
                "Temperature": 82.57854014653087
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_18_3",
                "RadialLocation": 18,
                "TangentialLocation": 3,
                "Temperature": 82.70241058196287
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_18_4",
                "RadialLocation": 18,
                "TangentialLocation": 4,
                "Temperature": 82.60821937096053
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_18_5",
                "RadialLocation": 18,
                "TangentialLocation": 5,
                "Temperature": 82.2636017180024
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_18_6",
                "RadialLocation": 18,
                "TangentialLocation": 6,
                "Temperature": 81.69352492995496
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_18_7",
                "RadialLocation": 18,
                "TangentialLocation": 7,
                "Temperature": 81.01241434811753
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "RotorWinding-Leading_Core_6_18_8",
                "RadialLocation": 18,
                "TangentialLocation": 8,
                "Temperature": 80.55215879373175
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 82.65816017735129
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_0_1",
                "RadialLocation": 0,
                "TangentialLocation": 1,
                "Temperature": 82.56467687932721
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_0_2",
                "RadialLocation": 0,
                "TangentialLocation": 2,
                "Temperature": 82.61354995914664
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_0_3",
                "RadialLocation": 0,
                "TangentialLocation": 3,
                "Temperature": 82.64687589800522
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_0_4",
                "RadialLocation": 0,
                "TangentialLocation": 4,
                "Temperature": 82.59322670525941
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_0_5",
                "RadialLocation": 0,
                "TangentialLocation": 5,
                "Temperature": 82.4298738685416
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_0_6",
                "RadialLocation": 0,
                "TangentialLocation": 6,
                "Temperature": 82.17317189695271
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_0_7",
                "RadialLocation": 0,
                "TangentialLocation": 7,
                "Temperature": 81.90791812049989
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_0_8",
                "RadialLocation": 0,
                "TangentialLocation": 8,
                "Temperature": 81.91866685481016
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 82.82332506756039
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_1_1",
                "RadialLocation": 1,
                "TangentialLocation": 1,
                "Temperature": 82.81027242887107
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_1_2",
                "RadialLocation": 1,
                "TangentialLocation": 2,
                "Temperature": 82.92663899723989
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_1_3",
                "RadialLocation": 1,
                "TangentialLocation": 3,
                "Temperature": 82.99279658669947
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_1_4",
                "RadialLocation": 1,
                "TangentialLocation": 4,
                "Temperature": 82.92265999176858
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_1_5",
                "RadialLocation": 1,
                "TangentialLocation": 5,
                "Temperature": 82.68886581887787
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_1_6",
                "RadialLocation": 1,
                "TangentialLocation": 6,
                "Temperature": 82.31475863313243
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_1_7",
                "RadialLocation": 1,
                "TangentialLocation": 7,
                "Temperature": 81.91172600169038
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_1_8",
                "RadialLocation": 1,
                "TangentialLocation": 8,
                "Temperature": 81.82985493979722
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 83.14281964316821
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_2_1",
                "RadialLocation": 2,
                "TangentialLocation": 1,
                "Temperature": 83.25406418733877
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_2_2",
                "RadialLocation": 2,
                "TangentialLocation": 2,
                "Temperature": 83.45369257450142
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_2_3",
                "RadialLocation": 2,
                "TangentialLocation": 3,
                "Temperature": 83.55984033143783
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_2_4",
                "RadialLocation": 2,
                "TangentialLocation": 4,
                "Temperature": 83.48358805764062
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_2_5",
                "RadialLocation": 2,
                "TangentialLocation": 5,
                "Temperature": 83.19765678154927
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_2_6",
                "RadialLocation": 2,
                "TangentialLocation": 6,
                "Temperature": 82.73063851821877
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_2_7",
                "RadialLocation": 2,
                "TangentialLocation": 7,
                "Temperature": 82.20698260560644
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_2_8",
                "RadialLocation": 2,
                "TangentialLocation": 8,
                "Temperature": 81.99995517608377
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 83.4733943477599
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_3_1",
                "RadialLocation": 3,
                "TangentialLocation": 1,
                "Temperature": 83.70984552789808
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_3_2",
                "RadialLocation": 3,
                "TangentialLocation": 2,
                "Temperature": 83.99138834614979
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_3_3",
                "RadialLocation": 3,
                "TangentialLocation": 3,
                "Temperature": 84.13826964565129
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_3_4",
                "RadialLocation": 3,
                "TangentialLocation": 4,
                "Temperature": 84.06231223594838
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_3_5",
                "RadialLocation": 3,
                "TangentialLocation": 5,
                "Temperature": 83.73777579504103
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_3_6",
                "RadialLocation": 3,
                "TangentialLocation": 6,
                "Temperature": 83.19685791319492
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_3_7",
                "RadialLocation": 3,
                "TangentialLocation": 7,
                "Temperature": 82.57001281633804
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_3_8",
                "RadialLocation": 3,
                "TangentialLocation": 8,
                "Temperature": 82.23728640339782
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 83.76417835618716
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_4_1",
                "RadialLocation": 4,
                "TangentialLocation": 1,
                "Temperature": 84.11009194962507
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_4_2",
                "RadialLocation": 4,
                "TangentialLocation": 2,
                "Temperature": 84.46366605581326
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_4_3",
                "RadialLocation": 4,
                "TangentialLocation": 3,
                "Temperature": 84.64768190855621
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_4_4",
                "RadialLocation": 4,
                "TangentialLocation": 4,
                "Temperature": 84.57524605724234
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_4_5",
                "RadialLocation": 4,
                "TangentialLocation": 5,
                "Temperature": 84.22214393422439
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_4_6",
                "RadialLocation": 4,
                "TangentialLocation": 6,
                "Temperature": 83.62291199874754
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_4_7",
                "RadialLocation": 4,
                "TangentialLocation": 7,
                "Temperature": 82.91075155992922
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_4_8",
                "RadialLocation": 4,
                "TangentialLocation": 8,
                "Temperature": 82.46682300320447
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 84.00042107404427
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_5_1",
                "RadialLocation": 5,
                "TangentialLocation": 1,
                "Temperature": 84.43506334914552
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_5_2",
                "RadialLocation": 5,
                "TangentialLocation": 2,
                "Temperature": 84.84757993049156
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_5_3",
                "RadialLocation": 5,
                "TangentialLocation": 3,
                "Temperature": 85.06285952713671
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_5_4",
                "RadialLocation": 5,
                "TangentialLocation": 4,
                "Temperature": 84.99502059888081
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_5_5",
                "RadialLocation": 5,
                "TangentialLocation": 5,
                "Temperature": 84.62096437807219
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_5_6",
                "RadialLocation": 5,
                "TangentialLocation": 6,
                "Temperature": 83.97671006581322
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_5_7",
                "RadialLocation": 5,
                "TangentialLocation": 7,
                "Temperature": 83.19678187339252
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_5_8",
                "RadialLocation": 5,
                "TangentialLocation": 8,
                "Temperature": 82.6617316819815
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 84.18093479974391
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_6_1",
                "RadialLocation": 6,
                "TangentialLocation": 1,
                "Temperature": 84.68327214173864
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_6_2",
                "RadialLocation": 6,
                "TangentialLocation": 2,
                "Temperature": 85.14111045069228
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_6_3",
                "RadialLocation": 6,
                "TangentialLocation": 3,
                "Temperature": 85.38092011388211
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_6_4",
                "RadialLocation": 6,
                "TangentialLocation": 4,
                "Temperature": 85.31747542722978
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_6_5",
                "RadialLocation": 6,
                "TangentialLocation": 5,
                "Temperature": 84.92839677154636
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_6_6",
                "RadialLocation": 6,
                "TangentialLocation": 6,
                "Temperature": 84.25063558617123
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_6_7",
                "RadialLocation": 6,
                "TangentialLocation": 7,
                "Temperature": 83.4194050958173
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_6_8",
                "RadialLocation": 6,
                "TangentialLocation": 8,
                "Temperature": 82.81429123169664
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 84.3089517841032
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_7_1",
                "RadialLocation": 7,
                "TangentialLocation": 1,
                "Temperature": 84.85922798155174
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_7_2",
                "RadialLocation": 7,
                "TangentialLocation": 2,
                "Temperature": 85.3493263112908
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_7_3",
                "RadialLocation": 7,
                "TangentialLocation": 3,
                "Temperature": 85.60682147361248
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_7_4",
                "RadialLocation": 7,
                "TangentialLocation": 4,
                "Temperature": 85.54687614856627
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_7_5",
                "RadialLocation": 7,
                "TangentialLocation": 5,
                "Temperature": 85.14754407036419
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_7_6",
                "RadialLocation": 7,
                "TangentialLocation": 6,
                "Temperature": 84.44635591630923
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_7_7",
                "RadialLocation": 7,
                "TangentialLocation": 7,
                "Temperature": 83.57891018943079
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_7_8",
                "RadialLocation": 7,
                "TangentialLocation": 8,
                "Temperature": 82.9239397893512
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 84.38836552897966
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_8_1",
                "RadialLocation": 8,
                "TangentialLocation": 1,
                "Temperature": 84.9683242205824
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_8_2",
                "RadialLocation": 8,
                "TangentialLocation": 2,
                "Temperature": 85.47843591572797
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_8_3",
                "RadialLocation": 8,
                "TangentialLocation": 3,
                "Temperature": 85.74695736141193
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_8_4",
                "RadialLocation": 8,
                "TangentialLocation": 4,
                "Temperature": 85.68926511994732
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_8_5",
                "RadialLocation": 8,
                "TangentialLocation": 5,
                "Temperature": 85.28366185878978
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_8_6",
                "RadialLocation": 8,
                "TangentialLocation": 6,
                "Temperature": 84.56802607338841
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_8_7",
                "RadialLocation": 8,
                "TangentialLocation": 7,
                "Temperature": 83.67818268166798
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_8_8",
                "RadialLocation": 8,
                "TangentialLocation": 8,
                "Temperature": 82.99229303242443
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 84.42218863392641
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_9_1",
                "RadialLocation": 9,
                "TangentialLocation": 1,
                "Temperature": 85.01472307650738
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_9_2",
                "RadialLocation": 9,
                "TangentialLocation": 2,
                "Temperature": 85.53326621732441
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_9_3",
                "RadialLocation": 9,
                "TangentialLocation": 3,
                "Temperature": 85.80636955613124
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_9_4",
                "RadialLocation": 9,
                "TangentialLocation": 4,
                "Temperature": 85.74950872008678
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_9_5",
                "RadialLocation": 9,
                "TangentialLocation": 5,
                "Temperature": 85.34111894209296
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_9_6",
                "RadialLocation": 9,
                "TangentialLocation": 6,
                "Temperature": 84.61926923840738
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_9_7",
                "RadialLocation": 9,
                "TangentialLocation": 7,
                "Temperature": 83.71992498406689
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_9_8",
                "RadialLocation": 9,
                "TangentialLocation": 8,
                "Temperature": 83.02102475156738
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 84.41196394812926
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_10_1",
                "RadialLocation": 10,
                "TangentialLocation": 1,
                "Temperature": 85.00054665550958
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_10_2",
                "RadialLocation": 10,
                "TangentialLocation": 2,
                "Temperature": 85.5162789272682
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_10_3",
                "RadialLocation": 10,
                "TangentialLocation": 3,
                "Temperature": 85.7876304016443
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_10_4",
                "RadialLocation": 10,
                "TangentialLocation": 4,
                "Temperature": 85.73008401991234
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_10_5",
                "RadialLocation": 10,
                "TangentialLocation": 5,
                "Temperature": 85.3221267286522
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_10_6",
                "RadialLocation": 10,
                "TangentialLocation": 6,
                "Temperature": 84.601906767161
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_10_7",
                "RadialLocation": 10,
                "TangentialLocation": 7,
                "Temperature": 83.70549143721426
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_10_8",
                "RadialLocation": 10,
                "TangentialLocation": 8,
                "Temperature": 83.01098169825917
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 84.35764070148637
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_11_1",
                "RadialLocation": 11,
                "TangentialLocation": 1,
                "Temperature": 84.925710188673
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_11_2",
                "RadialLocation": 11,
                "TangentialLocation": 2,
                "Temperature": 85.42736390754558
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_11_3",
                "RadialLocation": 11,
                "TangentialLocation": 3,
                "Temperature": 85.69059483222912
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_11_4",
                "RadialLocation": 11,
                "TangentialLocation": 4,
                "Temperature": 85.63078645952145
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_11_5",
                "RadialLocation": 11,
                "TangentialLocation": 5,
                "Temperature": 85.22640300883839
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_11_6",
                "RadialLocation": 11,
                "TangentialLocation": 6,
                "Temperature": 84.51559174123776
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_11_7",
                "RadialLocation": 11,
                "TangentialLocation": 7,
                "Temperature": 83.6345292218516
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_11_8",
                "RadialLocation": 11,
                "TangentialLocation": 8,
                "Temperature": 82.96189925425828
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 84.2577894634811
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_12_1",
                "RadialLocation": 12,
                "TangentialLocation": 1,
                "Temperature": 84.78822805474542
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_12_2",
                "RadialLocation": 12,
                "TangentialLocation": 2,
                "Temperature": 85.26421640258229
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_12_3",
                "RadialLocation": 12,
                "TangentialLocation": 3,
                "Temperature": 85.51281688942015
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_12_4",
                "RadialLocation": 12,
                "TangentialLocation": 4,
                "Temperature": 85.44914399511254
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_12_5",
                "RadialLocation": 12,
                "TangentialLocation": 5,
                "Temperature": 85.05154138506103
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_12_6",
                "RadialLocation": 12,
                "TangentialLocation": 6,
                "Temperature": 84.35810174304018
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_12_7",
                "RadialLocation": 12,
                "TangentialLocation": 7,
                "Temperature": 83.5051823687246
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_12_8",
                "RadialLocation": 12,
                "TangentialLocation": 8,
                "Temperature": 82.87252443710972
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 84.11028628868215
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_13_1",
                "RadialLocation": 13,
                "TangentialLocation": 1,
                "Temperature": 84.58517964221926
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_13_2",
                "RadialLocation": 13,
                "TangentialLocation": 2,
                "Temperature": 85.02352601603275
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_13_3",
                "RadialLocation": 13,
                "TangentialLocation": 3,
                "Temperature": 85.25088038668723
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_13_4",
                "RadialLocation": 13,
                "TangentialLocation": 4,
                "Temperature": 85.18178862931627
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_13_5",
                "RadialLocation": 13,
                "TangentialLocation": 5,
                "Temperature": 84.79431762525608
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_13_6",
                "RadialLocation": 13,
                "TangentialLocation": 6,
                "Temperature": 84.12648298708636
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_13_7",
                "RadialLocation": 13,
                "TangentialLocation": 7,
                "Temperature": 83.31499810200022
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_13_8",
                "RadialLocation": 13,
                "TangentialLocation": 8,
                "Temperature": 82.74122952072825
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 83.91393656121964
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_14_1",
                "RadialLocation": 14,
                "TangentialLocation": 1,
                "Temperature": 84.314991405944
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_14_2",
                "RadialLocation": 14,
                "TangentialLocation": 2,
                "Temperature": 84.70375389059701
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_14_3",
                "RadialLocation": 14,
                "TangentialLocation": 3,
                "Temperature": 84.90348012169079
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_14_4",
                "RadialLocation": 14,
                "TangentialLocation": 4,
                "Temperature": 84.82763228670403
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_14_5",
                "RadialLocation": 14,
                "TangentialLocation": 5,
                "Temperature": 84.45374696488527
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_14_6",
                "RadialLocation": 14,
                "TangentialLocation": 6,
                "Temperature": 83.81978038294257
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_14_7",
                "RadialLocation": 14,
                "TangentialLocation": 7,
                "Temperature": 83.06313573396744
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_14_8",
                "RadialLocation": 14,
                "TangentialLocation": 8,
                "Temperature": 82.56752263286154
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 83.67213124311368
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_15_1",
                "RadialLocation": 15,
                "TangentialLocation": 1,
                "Temperature": 83.98252407390329
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_15_2",
                "RadialLocation": 15,
                "TangentialLocation": 2,
                "Temperature": 84.3112109568765
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_15_3",
                "RadialLocation": 15,
                "TangentialLocation": 3,
                "Temperature": 84.47806172806108
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_15_4",
                "RadialLocation": 15,
                "TangentialLocation": 4,
                "Temperature": 84.39466534856547
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_15_5",
                "RadialLocation": 15,
                "TangentialLocation": 5,
                "Temperature": 84.03765506733752
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_15_6",
                "RadialLocation": 15,
                "TangentialLocation": 6,
                "Temperature": 83.444982051541
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_15_7",
                "RadialLocation": 15,
                "TangentialLocation": 7,
                "Temperature": 82.75525352322845
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_15_8",
                "RadialLocation": 15,
                "TangentialLocation": 8,
                "Temperature": 82.35541351026254
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 83.40064817636261
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_16_1",
                "RadialLocation": 16,
                "TangentialLocation": 1,
                "Temperature": 83.60973956659413
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_16_2",
                "RadialLocation": 16,
                "TangentialLocation": 2,
                "Temperature": 83.8725022980684
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_16_3",
                "RadialLocation": 16,
                "TangentialLocation": 3,
                "Temperature": 84.00416114159074
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_16_4",
                "RadialLocation": 16,
                "TangentialLocation": 4,
                "Temperature": 83.91349259818251
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_16_5",
                "RadialLocation": 16,
                "TangentialLocation": 5,
                "Temperature": 83.57579150776056
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_16_6",
                "RadialLocation": 16,
                "TangentialLocation": 6,
                "Temperature": 83.02903538137033
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_16_7",
                "RadialLocation": 16,
                "TangentialLocation": 7,
                "Temperature": 82.41357255237062
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_16_8",
                "RadialLocation": 16,
                "TangentialLocation": 8,
                "Temperature": 82.12043662602193
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 83.14188318784343
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_17_1",
                "RadialLocation": 17,
                "TangentialLocation": 1,
                "Temperature": 83.25466515816598
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_17_2",
                "RadialLocation": 17,
                "TangentialLocation": 2,
                "Temperature": 83.45601609083904
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_17_3",
                "RadialLocation": 17,
                "TangentialLocation": 3,
                "Temperature": 83.55593771625804
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_17_4",
                "RadialLocation": 17,
                "TangentialLocation": 4,
                "Temperature": 83.45992531884895
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_17_5",
                "RadialLocation": 17,
                "TangentialLocation": 5,
                "Temperature": 83.14168839414505
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_17_6",
                "RadialLocation": 17,
                "TangentialLocation": 6,
                "Temperature": 82.63907577361803
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_17_7",
                "RadialLocation": 17,
                "TangentialLocation": 7,
                "Temperature": 82.09414745869537
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_17_8",
                "RadialLocation": 17,
                "TangentialLocation": 8,
                "Temperature": 81.90192896870234
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 82.97747286678201
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_18_1",
                "RadialLocation": 18,
                "TangentialLocation": 1,
                "Temperature": 83.02762391706571
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_18_2",
                "RadialLocation": 18,
                "TangentialLocation": 2,
                "Temperature": 83.18946534772734
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_18_3",
                "RadialLocation": 18,
                "TangentialLocation": 3,
                "Temperature": 83.26975486527401
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_18_4",
                "RadialLocation": 18,
                "TangentialLocation": 4,
                "Temperature": 83.17184643980445
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_18_5",
                "RadialLocation": 18,
                "TangentialLocation": 5,
                "Temperature": 82.86827469068751
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_18_6",
                "RadialLocation": 18,
                "TangentialLocation": 6,
                "Temperature": 82.3963454143129
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_18_7",
                "RadialLocation": 18,
                "TangentialLocation": 7,
                "Temperature": 81.89847081321597
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "RotorWinding-Leading_Core_7_18_8",
                "RadialLocation": 18,
                "TangentialLocation": 8,
                "Temperature": 81.77107828025542
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 83.38321021650044
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_0_1",
                "RadialLocation": 0,
                "TangentialLocation": 1,
                "Temperature": 83.2495537049352
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_0_2",
                "RadialLocation": 0,
                "TangentialLocation": 2,
                "Temperature": 83.25780312299185
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_0_3",
                "RadialLocation": 0,
                "TangentialLocation": 3,
                "Temperature": 83.26647182378328
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_0_4",
                "RadialLocation": 0,
                "TangentialLocation": 4,
                "Temperature": 83.2093630488136
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_0_5",
                "RadialLocation": 0,
                "TangentialLocation": 5,
                "Temperature": 83.06761321403147
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_0_6",
                "RadialLocation": 0,
                "TangentialLocation": 6,
                "Temperature": 82.86563163693071
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_0_7",
                "RadialLocation": 0,
                "TangentialLocation": 7,
                "Temperature": 82.70437266093114
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_0_8",
                "RadialLocation": 0,
                "TangentialLocation": 8,
                "Temperature": 82.91042395815927
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 83.44223746379929
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_1_1",
                "RadialLocation": 1,
                "TangentialLocation": 1,
                "Temperature": 83.35936989172467
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_1_2",
                "RadialLocation": 1,
                "TangentialLocation": 2,
                "Temperature": 83.41623310825958
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_1_3",
                "RadialLocation": 1,
                "TangentialLocation": 3,
                "Temperature": 83.4480003213492
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_1_4",
                "RadialLocation": 1,
                "TangentialLocation": 4,
                "Temperature": 83.37404258674212
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_1_5",
                "RadialLocation": 1,
                "TangentialLocation": 5,
                "Temperature": 83.17163073088615
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_1_6",
                "RadialLocation": 1,
                "TangentialLocation": 6,
                "Temperature": 82.87363068610486
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_1_7",
                "RadialLocation": 1,
                "TangentialLocation": 7,
                "Temperature": 82.60907547063275
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_1_8",
                "RadialLocation": 1,
                "TangentialLocation": 8,
                "Temperature": 82.76747302417766
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 83.69256825459965
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_2_1",
                "RadialLocation": 2,
                "TangentialLocation": 1,
                "Temperature": 83.70892625125698
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_2_2",
                "RadialLocation": 2,
                "TangentialLocation": 2,
                "Temperature": 83.83432943863123
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_2_3",
                "RadialLocation": 2,
                "TangentialLocation": 3,
                "Temperature": 83.8988974050606
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_2_4",
                "RadialLocation": 2,
                "TangentialLocation": 4,
                "Temperature": 83.81807516808817
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_2_5",
                "RadialLocation": 2,
                "TangentialLocation": 5,
                "Temperature": 83.56915131633441
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_2_6",
                "RadialLocation": 2,
                "TangentialLocation": 6,
                "Temperature": 83.19082549875341
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_2_7",
                "RadialLocation": 2,
                "TangentialLocation": 7,
                "Temperature": 82.82604010733732
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_2_8",
                "RadialLocation": 2,
                "TangentialLocation": 8,
                "Temperature": 82.88740781979548
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 83.98031222181734
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_3_1",
                "RadialLocation": 3,
                "TangentialLocation": 1,
                "Temperature": 84.10348826874169
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_3_2",
                "RadialLocation": 3,
                "TangentialLocation": 2,
                "Temperature": 84.3001270138113
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_3_3",
                "RadialLocation": 3,
                "TangentialLocation": 3,
                "Temperature": 84.40024581081994
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_3_4",
                "RadialLocation": 3,
                "TangentialLocation": 4,
                "Temperature": 84.31887679830608
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_3_5",
                "RadialLocation": 3,
                "TangentialLocation": 5,
                "Temperature": 84.03457235143452
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_3_6",
                "RadialLocation": 3,
                "TangentialLocation": 6,
                "Temperature": 83.58995535429683
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_3_7",
                "RadialLocation": 3,
                "TangentialLocation": 7,
                "Temperature": 83.13484347127242
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_3_8",
                "RadialLocation": 3,
                "TangentialLocation": 8,
                "Temperature": 83.08985634493388
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 84.24626495548064
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_4_1",
                "RadialLocation": 4,
                "TangentialLocation": 1,
                "Temperature": 84.46620015098577
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_4_2",
                "RadialLocation": 4,
                "TangentialLocation": 2,
                "Temperature": 84.72747960107198
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_4_3",
                "RadialLocation": 4,
                "TangentialLocation": 3,
                "Temperature": 84.86113130256912
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_4_4",
                "RadialLocation": 4,
                "TangentialLocation": 4,
                "Temperature": 84.78256136603356
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_4_5",
                "RadialLocation": 4,
                "TangentialLocation": 5,
                "Temperature": 84.47159141168699
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_4_6",
                "RadialLocation": 4,
                "TangentialLocation": 6,
                "Temperature": 83.97340466459617
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_4_7",
                "RadialLocation": 4,
                "TangentialLocation": 7,
                "Temperature": 83.44135091637472
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_4_8",
                "RadialLocation": 4,
                "TangentialLocation": 8,
                "Temperature": 83.29843168553066
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 84.46892000003109
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_5_1",
                "RadialLocation": 5,
                "TangentialLocation": 1,
                "Temperature": 84.76906537469154
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_5_2",
                "RadialLocation": 5,
                "TangentialLocation": 2,
                "Temperature": 85.0843254016867
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_5_3",
                "RadialLocation": 5,
                "TangentialLocation": 3,
                "Temperature": 85.24681806328182
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_5_4",
                "RadialLocation": 5,
                "TangentialLocation": 4,
                "Temperature": 85.17230091864988
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_5_5",
                "RadialLocation": 5,
                "TangentialLocation": 5,
                "Temperature": 84.84151952080379
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_5_6",
                "RadialLocation": 5,
                "TangentialLocation": 6,
                "Temperature": 84.30130850522264
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_5_7",
                "RadialLocation": 5,
                "TangentialLocation": 7,
                "Temperature": 83.70697172560074
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_5_8",
                "RadialLocation": 5,
                "TangentialLocation": 8,
                "Temperature": 83.48188263859397
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 84.64242444231279
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_6_1",
                "RadialLocation": 6,
                "TangentialLocation": 1,
                "Temperature": 85.00468789052543
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_6_2",
                "RadialLocation": 6,
                "TangentialLocation": 2,
                "Temperature": 85.3620271211413
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_6_3",
                "RadialLocation": 6,
                "TangentialLocation": 3,
                "Temperature": 85.5474709183084
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_6_4",
                "RadialLocation": 6,
                "TangentialLocation": 4,
                "Temperature": 85.4769702622539
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_6_5",
                "RadialLocation": 6,
                "TangentialLocation": 5,
                "Temperature": 85.13185705368785
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_6_6",
                "RadialLocation": 6,
                "TangentialLocation": 6,
                "Temperature": 84.56002524731292
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_6_7",
                "RadialLocation": 6,
                "TangentialLocation": 7,
                "Temperature": 83.91793909319075
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_6_8",
                "RadialLocation": 6,
                "TangentialLocation": 8,
                "Temperature": 83.62869326289254
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 84.76708789779174
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_7_1",
                "RadialLocation": 7,
                "TangentialLocation": 1,
                "Temperature": 85.17378574755273
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_7_2",
                "RadialLocation": 7,
                "TangentialLocation": 2,
                "Temperature": 85.56135598621223
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_7_3",
                "RadialLocation": 7,
                "TangentialLocation": 3,
                "Temperature": 85.76350357950743
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_7_4",
                "RadialLocation": 7,
                "TangentialLocation": 4,
                "Temperature": 85.69625911516327
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_7_5",
                "RadialLocation": 7,
                "TangentialLocation": 5,
                "Temperature": 85.3413008900441
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_7_6",
                "RadialLocation": 7,
                "TangentialLocation": 6,
                "Temperature": 84.74719194125358
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_7_7",
                "RadialLocation": 7,
                "TangentialLocation": 7,
                "Temperature": 84.07110864764005
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_7_8",
                "RadialLocation": 7,
                "TangentialLocation": 8,
                "Temperature": 83.73574245490013
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 84.84510634440147
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_8_1",
                "RadialLocation": 8,
                "TangentialLocation": 1,
                "Temperature": 85.2795049449334
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_8_2",
                "RadialLocation": 8,
                "TangentialLocation": 2,
                "Temperature": 85.68594738110083
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_8_3",
                "RadialLocation": 8,
                "TangentialLocation": 3,
                "Temperature": 85.89857396468169
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_8_4",
                "RadialLocation": 8,
                "TangentialLocation": 4,
                "Temperature": 85.83344488987329
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_8_5",
                "RadialLocation": 8,
                "TangentialLocation": 5,
                "Temperature": 85.47243614639504
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_8_6",
                "RadialLocation": 8,
                "TangentialLocation": 6,
                "Temperature": 84.8645138218011
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_8_7",
                "RadialLocation": 8,
                "TangentialLocation": 7,
                "Temperature": 84.16727912209487
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_8_8",
                "RadialLocation": 8,
                "TangentialLocation": 8,
                "Temperature": 83.80311313778547
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 84.87861628773767
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_9_1",
                "RadialLocation": 9,
                "TangentialLocation": 1,
                "Temperature": 85.32482595926797
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_9_2",
                "RadialLocation": 9,
                "TangentialLocation": 2,
                "Temperature": 85.73926357967896
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_9_3",
                "RadialLocation": 9,
                "TangentialLocation": 3,
                "Temperature": 85.9562664436004
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_9_4",
                "RadialLocation": 9,
                "TangentialLocation": 4,
                "Temperature": 85.89191769506316
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_9_5",
                "RadialLocation": 9,
                "TangentialLocation": 5,
                "Temperature": 85.52820442441539
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_9_6",
                "RadialLocation": 9,
                "TangentialLocation": 6,
                "Temperature": 84.91430535383087
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_9_7",
                "RadialLocation": 9,
                "TangentialLocation": 7,
                "Temperature": 84.20804275175914
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_9_8",
                "RadialLocation": 9,
                "TangentialLocation": 8,
                "Temperature": 83.83167695750214
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 84.86886513179199
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_10_1",
                "RadialLocation": 10,
                "TangentialLocation": 1,
                "Temperature": 85.31146131765134
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_10_2",
                "RadialLocation": 10,
                "TangentialLocation": 2,
                "Temperature": 85.72328819749303
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_10_3",
                "RadialLocation": 10,
                "TangentialLocation": 3,
                "Temperature": 85.93864071999752
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_10_4",
                "RadialLocation": 10,
                "TangentialLocation": 4,
                "Temperature": 85.87363514625339
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_10_5",
                "RadialLocation": 10,
                "TangentialLocation": 5,
                "Temperature": 85.5103161371124
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_10_6",
                "RadialLocation": 10,
                "TangentialLocation": 6,
                "Temperature": 84.89793074682343
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_10_7",
                "RadialLocation": 10,
                "TangentialLocation": 7,
                "Temperature": 84.19436952211221
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_10_8",
                "RadialLocation": 10,
                "TangentialLocation": 8,
                "Temperature": 83.82200838634944
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 84.8159952988885
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_11_1",
                "RadialLocation": 11,
                "TangentialLocation": 1,
                "Temperature": 85.239574125368
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_11_2",
                "RadialLocation": 11,
                "TangentialLocation": 2,
                "Temperature": 85.63819195609855
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_11_3",
                "RadialLocation": 11,
                "TangentialLocation": 3,
                "Temperature": 85.84585048771933
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_11_4",
                "RadialLocation": 11,
                "TangentialLocation": 4,
                "Temperature": 85.77869719125982
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_11_5",
                "RadialLocation": 11,
                "TangentialLocation": 5,
                "Temperature": 85.41878777996762
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_11_6",
                "RadialLocation": 11,
                "TangentialLocation": 6,
                "Temperature": 84.81532267559871
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_11_7",
                "RadialLocation": 11,
                "TangentialLocation": 7,
                "Temperature": 84.12614927938857
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_11_8",
                "RadialLocation": 11,
                "TangentialLocation": 8,
                "Temperature": 83.77402215271002
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 84.7192986335746
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_12_1",
                "RadialLocation": 12,
                "TangentialLocation": 1,
                "Temperature": 85.10812885411391
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_12_2",
                "RadialLocation": 12,
                "TangentialLocation": 2,
                "Temperature": 85.48275652128602
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_12_3",
                "RadialLocation": 12,
                "TangentialLocation": 3,
                "Temperature": 85.67660729603925
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_12_4",
                "RadialLocation": 12,
                "TangentialLocation": 4,
                "Temperature": 85.60580849330292
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_12_5",
                "RadialLocation": 12,
                "TangentialLocation": 5,
                "Temperature": 85.25236090094673
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_12_6",
                "RadialLocation": 12,
                "TangentialLocation": 6,
                "Temperature": 84.66532543928088
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_12_7",
                "RadialLocation": 12,
                "TangentialLocation": 7,
                "Temperature": 84.00244446914614
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_12_8",
                "RadialLocation": 12,
                "TangentialLocation": 8,
                "Temperature": 83.68713746397192
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 84.57805790091106
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_13_1",
                "RadialLocation": 13,
                "TangentialLocation": 1,
                "Temperature": 84.91603995512293
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_13_2",
                "RadialLocation": 13,
                "TangentialLocation": 2,
                "Temperature": 85.25575678571775
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_13_3",
                "RadialLocation": 13,
                "TangentialLocation": 3,
                "Temperature": 85.42970845248469
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_13_4",
                "RadialLocation": 13,
                "TangentialLocation": 4,
                "Temperature": 85.35384837659564
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_13_5",
                "RadialLocation": 13,
                "TangentialLocation": 5,
                "Temperature": 85.01000632621219
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_13_6",
                "RadialLocation": 13,
                "TangentialLocation": 6,
                "Temperature": 84.44703302277672
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_13_7",
                "RadialLocation": 13,
                "TangentialLocation": 7,
                "Temperature": 83.82257882802263
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_13_8",
                "RadialLocation": 13,
                "TangentialLocation": 8,
                "Temperature": 83.56104591116117
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 84.39340261412225
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_14_1",
                "RadialLocation": 14,
                "TangentialLocation": 1,
                "Temperature": 84.66470524329922
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_14_2",
                "RadialLocation": 14,
                "TangentialLocation": 2,
                "Temperature": 84.95898961579319
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_14_3",
                "RadialLocation": 14,
                "TangentialLocation": 3,
                "Temperature": 85.10736651831611
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_14_4",
                "RadialLocation": 14,
                "TangentialLocation": 4,
                "Temperature": 85.02529474128929
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_14_5",
                "RadialLocation": 14,
                "TangentialLocation": 5,
                "Temperature": 84.69423367964876
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_14_6",
                "RadialLocation": 14,
                "TangentialLocation": 6,
                "Temperature": 84.16277693399687
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_14_7",
                "RadialLocation": 14,
                "TangentialLocation": 7,
                "Temperature": 83.58860377889424
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_14_8",
                "RadialLocation": 14,
                "TangentialLocation": 8,
                "Temperature": 83.39745745272705
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 84.17208575200546
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_15_1",
                "RadialLocation": 15,
                "TangentialLocation": 1,
                "Temperature": 84.36314310838627
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_15_2",
                "RadialLocation": 15,
                "TangentialLocation": 2,
                "Temperature": 84.60333791934572
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_15_3",
                "RadialLocation": 15,
                "TangentialLocation": 3,
                "Temperature": 84.72179753759292
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_15_4",
                "RadialLocation": 15,
                "TangentialLocation": 4,
                "Temperature": 84.6329657416653
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_15_5",
                "RadialLocation": 15,
                "TangentialLocation": 5,
                "Temperature": 84.31763191550424
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_15_6",
                "RadialLocation": 15,
                "TangentialLocation": 6,
                "Temperature": 83.82409378856119
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_15_7",
                "RadialLocation": 15,
                "TangentialLocation": 7,
                "Temperature": 83.31028061998796
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_15_8",
                "RadialLocation": 15,
                "TangentialLocation": 8,
                "Temperature": 83.20363161208847
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 83.93367553227766
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_16_1",
                "RadialLocation": 16,
                "TangentialLocation": 1,
                "Temperature": 84.03765699383412
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_16_2",
                "RadialLocation": 16,
                "TangentialLocation": 2,
                "Temperature": 84.21995013202601
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_16_3",
                "RadialLocation": 16,
                "TangentialLocation": 3,
                "Temperature": 84.30716422797481
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_16_4",
                "RadialLocation": 16,
                "TangentialLocation": 4,
                "Temperature": 84.21214574209809
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_16_5",
                "RadialLocation": 16,
                "TangentialLocation": 5,
                "Temperature": 83.91466722405164
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_16_6",
                "RadialLocation": 16,
                "TangentialLocation": 6,
                "Temperature": 83.46262381738696
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_16_7",
                "RadialLocation": 16,
                "TangentialLocation": 7,
                "Temperature": 83.01433006655945
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_16_8",
                "RadialLocation": 16,
                "TangentialLocation": 8,
                "Temperature": 82.99898916530465
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 83.72192024575925
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_17_1",
                "RadialLocation": 17,
                "TangentialLocation": 1,
                "Temperature": 83.74671532048173
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_17_2",
                "RadialLocation": 17,
                "TangentialLocation": 2,
                "Temperature": 83.87692929621028
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_17_3",
                "RadialLocation": 17,
                "TangentialLocation": 3,
                "Temperature": 83.93698188593302
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_17_4",
                "RadialLocation": 17,
                "TangentialLocation": 4,
                "Temperature": 83.83803262722135
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_17_5",
                "RadialLocation": 17,
                "TangentialLocation": 5,
                "Temperature": 83.55865818135916
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_17_6",
                "RadialLocation": 17,
                "TangentialLocation": 6,
                "Temperature": 83.14599815234855
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_17_7",
                "RadialLocation": 17,
                "TangentialLocation": 7,
                "Temperature": 82.75822251081264
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_17_8",
                "RadialLocation": 17,
                "TangentialLocation": 8,
                "Temperature": 82.82516552303926
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 83.60929805254985
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_18_1",
                "RadialLocation": 18,
                "TangentialLocation": 1,
                "Temperature": 83.58649393044897
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_18_2",
                "RadialLocation": 18,
                "TangentialLocation": 2,
                "Temperature": 83.68484173259407
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_18_3",
                "RadialLocation": 18,
                "TangentialLocation": 3,
                "Temperature": 83.72906991814406
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_18_4",
                "RadialLocation": 18,
                "TangentialLocation": 4,
                "Temperature": 83.62989577559932
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_18_5",
                "RadialLocation": 18,
                "TangentialLocation": 5,
                "Temperature": 83.3650725794937
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_18_6",
                "RadialLocation": 18,
                "TangentialLocation": 6,
                "Temperature": 82.98036021315166
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_18_7",
                "RadialLocation": 18,
                "TangentialLocation": 7,
                "Temperature": 82.63201866790637
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "RotorWinding-Leading_Core_8_18_8",
                "RadialLocation": 18,
                "TangentialLocation": 8,
                "Temperature": 82.74705010012894
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 83.9142740485743
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_0_1",
                "RadialLocation": 0,
                "TangentialLocation": 1,
                "Temperature": 83.75624376763618
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_0_2",
                "RadialLocation": 0,
                "TangentialLocation": 2,
                "Temperature": 83.73358726727699
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_0_3",
                "RadialLocation": 0,
                "TangentialLocation": 3,
                "Temperature": 83.72235208040583
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_0_4",
                "RadialLocation": 0,
                "TangentialLocation": 4,
                "Temperature": 83.66220357213899
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_0_5",
                "RadialLocation": 0,
                "TangentialLocation": 5,
                "Temperature": 83.53793006900965
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_0_6",
                "RadialLocation": 0,
                "TangentialLocation": 6,
                "Temperature": 83.37931029825693
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_0_7",
                "RadialLocation": 0,
                "TangentialLocation": 7,
                "Temperature": 83.29184590022147
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_0_8",
                "RadialLocation": 0,
                "TangentialLocation": 8,
                "Temperature": 83.5960601526625
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 83.90216171090456
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_1_1",
                "RadialLocation": 1,
                "TangentialLocation": 1,
                "Temperature": 83.77415241696282
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_1_2",
                "RadialLocation": 1,
                "TangentialLocation": 2,
                "Temperature": 83.78549437346757
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_1_3",
                "RadialLocation": 1,
                "TangentialLocation": 3,
                "Temperature": 83.78971473610355
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_1_4",
                "RadialLocation": 1,
                "TangentialLocation": 4,
                "Temperature": 83.71324593652459
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_1_5",
                "RadialLocation": 1,
                "TangentialLocation": 5,
                "Temperature": 83.53788067662143
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_1_6",
                "RadialLocation": 1,
                "TangentialLocation": 6,
                "Temperature": 83.30236969857835
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_1_7",
                "RadialLocation": 1,
                "TangentialLocation": 7,
                "Temperature": 83.13896711958392
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_1_8",
                "RadialLocation": 1,
                "TangentialLocation": 8,
                "Temperature": 83.42284417304906
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 84.099551444538
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_2_1",
                "RadialLocation": 2,
                "TangentialLocation": 1,
                "Temperature": 84.0490236702856
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_2_2",
                "RadialLocation": 2,
                "TangentialLocation": 2,
                "Temperature": 84.11613612151572
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_2_3",
                "RadialLocation": 2,
                "TangentialLocation": 3,
                "Temperature": 84.14693511802906
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_2_4",
                "RadialLocation": 2,
                "TangentialLocation": 4,
                "Temperature": 84.06316444371673
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_2_5",
                "RadialLocation": 2,
                "TangentialLocation": 5,
                "Temperature": 83.84661499084717
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_2_6",
                "RadialLocation": 2,
                "TangentialLocation": 6,
                "Temperature": 83.54218162605663
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_2_7",
                "RadialLocation": 2,
                "TangentialLocation": 7,
                "Temperature": 83.29615954863276
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_2_8",
                "RadialLocation": 2,
                "TangentialLocation": 8,
                "Temperature": 83.50583537827391
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 84.35375018592521
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_3_1",
                "RadialLocation": 3,
                "TangentialLocation": 1,
                "Temperature": 84.39231569021761
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_3_2",
                "RadialLocation": 3,
                "TangentialLocation": 2,
                "Temperature": 84.5207879635123
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_3_3",
                "RadialLocation": 3,
                "TangentialLocation": 3,
                "Temperature": 84.58240155609472
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_3_4",
                "RadialLocation": 3,
                "TangentialLocation": 4,
                "Temperature": 84.49737601340304
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_3_5",
                "RadialLocation": 3,
                "TangentialLocation": 5,
                "Temperature": 84.24850358142393
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_3_6",
                "RadialLocation": 3,
                "TangentialLocation": 6,
                "Temperature": 83.88484541677582
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_3_7",
                "RadialLocation": 3,
                "TangentialLocation": 7,
                "Temperature": 83.56030037706556
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_3_8",
                "RadialLocation": 3,
                "TangentialLocation": 8,
                "Temperature": 83.68170612357441
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 84.60080482383374
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_4_1",
                "RadialLocation": 4,
                "TangentialLocation": 1,
                "Temperature": 84.7229401283965
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_4_2",
                "RadialLocation": 4,
                "TangentialLocation": 2,
                "Temperature": 84.90891353511611
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_4_3",
                "RadialLocation": 4,
                "TangentialLocation": 3,
                "Temperature": 85.00065116176208
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_4_4",
                "RadialLocation": 4,
                "TangentialLocation": 4,
                "Temperature": 84.91776010967499
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_4_5",
                "RadialLocation": 4,
                "TangentialLocation": 5,
                "Temperature": 84.64403765284153
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_4_6",
                "RadialLocation": 4,
                "TangentialLocation": 6,
                "Temperature": 84.23131837539601
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_4_7",
                "RadialLocation": 4,
                "TangentialLocation": 7,
                "Temperature": 83.8378694859105
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_4_8",
                "RadialLocation": 4,
                "TangentialLocation": 8,
                "Temperature": 83.87493213726718
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 84.81387740658104
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_5_1",
                "RadialLocation": 5,
                "TangentialLocation": 1,
                "Temperature": 85.0068266350752
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_5_2",
                "RadialLocation": 5,
                "TangentialLocation": 2,
                "Temperature": 85.24182100800597
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_5_3",
                "RadialLocation": 5,
                "TangentialLocation": 3,
                "Temperature": 85.36004566925057
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_5_4",
                "RadialLocation": 5,
                "TangentialLocation": 4,
                "Temperature": 85.28068553124666
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_5_5",
                "RadialLocation": 5,
                "TangentialLocation": 5,
                "Temperature": 84.98825452553584
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_5_6",
                "RadialLocation": 5,
                "TangentialLocation": 6,
                "Temperature": 84.53642068048185
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_5_7",
                "RadialLocation": 5,
                "TangentialLocation": 7,
                "Temperature": 84.08614878087619
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_5_8",
                "RadialLocation": 5,
                "TangentialLocation": 8,
                "Temperature": 84.05087472210923
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 84.98311440904722
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_6_1",
                "RadialLocation": 6,
                "TangentialLocation": 1,
                "Temperature": 85.23170831532059
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_6_2",
                "RadialLocation": 6,
                "TangentialLocation": 2,
                "Temperature": 85.50544816073867
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_6_3",
                "RadialLocation": 6,
                "TangentialLocation": 3,
                "Temperature": 85.64505715396155
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_6_4",
                "RadialLocation": 6,
                "TangentialLocation": 4,
                "Temperature": 85.56934178817393
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_6_5",
                "RadialLocation": 6,
                "TangentialLocation": 5,
                "Temperature": 85.26325358734918
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_6_6",
                "RadialLocation": 6,
                "TangentialLocation": 6,
                "Temperature": 84.7816651285105
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_6_7",
                "RadialLocation": 6,
                "TangentialLocation": 7,
                "Temperature": 84.28729003909433
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_6_8",
                "RadialLocation": 6,
                "TangentialLocation": 8,
                "Temperature": 84.19472886767036
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 85.1062446226044
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_7_1",
                "RadialLocation": 7,
                "TangentialLocation": 1,
                "Temperature": 85.39503101776737
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_7_2",
                "RadialLocation": 7,
                "TangentialLocation": 2,
                "Temperature": 85.6968667238167
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_7_3",
                "RadialLocation": 7,
                "TangentialLocation": 3,
                "Temperature": 85.8521883108693
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_7_4",
                "RadialLocation": 7,
                "TangentialLocation": 4,
                "Temperature": 85.7794855015965
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_7_5",
                "RadialLocation": 7,
                "TangentialLocation": 5,
                "Temperature": 85.46395614738165
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_7_6",
                "RadialLocation": 7,
                "TangentialLocation": 6,
                "Temperature": 84.96124775354058
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_7_7",
                "RadialLocation": 7,
                "TangentialLocation": 7,
                "Temperature": 84.43520940575763
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_7_8",
                "RadialLocation": 7,
                "TangentialLocation": 8,
                "Temperature": 84.30107626095095
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 85.18395212625201
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_8_1",
                "RadialLocation": 8,
                "TangentialLocation": 1,
                "Temperature": 85.49795870407318
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_8_2",
                "RadialLocation": 8,
                "TangentialLocation": 2,
                "Temperature": 85.81744286934065
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_8_3",
                "RadialLocation": 8,
                "TangentialLocation": 3,
                "Temperature": 85.98268290937882
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_8_4",
                "RadialLocation": 8,
                "TangentialLocation": 4,
                "Temperature": 85.91195557451206
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_8_5",
                "RadialLocation": 8,
                "TangentialLocation": 5,
                "Temperature": 85.5905963177869
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_8_6",
                "RadialLocation": 8,
                "TangentialLocation": 6,
                "Temperature": 85.07472193791918
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_8_7",
                "RadialLocation": 8,
                "TangentialLocation": 7,
                "Temperature": 84.52886965299119
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_8_8",
                "RadialLocation": 8,
                "TangentialLocation": 8,
                "Temperature": 84.36861010261227
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 85.21759474801226
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_9_1",
                "RadialLocation": 9,
                "TangentialLocation": 1,
                "Temperature": 85.54241871976652
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_9_2",
                "RadialLocation": 9,
                "TangentialLocation": 2,
                "Temperature": 85.86941991315952
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_9_3",
                "RadialLocation": 9,
                "TangentialLocation": 3,
                "Temperature": 86.0388219390228
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_9_4",
                "RadialLocation": 9,
                "TangentialLocation": 4,
                "Temperature": 85.96882199809778
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_9_5",
                "RadialLocation": 9,
                "TangentialLocation": 5,
                "Temperature": 85.64484108226237
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_9_6",
                "RadialLocation": 9,
                "TangentialLocation": 6,
                "Temperature": 85.12323565990886
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_9_7",
                "RadialLocation": 9,
                "TangentialLocation": 7,
                "Temperature": 84.56887358973259
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_9_8",
                "RadialLocation": 9,
                "TangentialLocation": 8,
                "Temperature": 84.3974753056602
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 85.20816102252707
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_10_1",
                "RadialLocation": 10,
                "TangentialLocation": 1,
                "Temperature": 85.5297565138019
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_10_2",
                "RadialLocation": 10,
                "TangentialLocation": 2,
                "Temperature": 85.85435047403365
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_10_3",
                "RadialLocation": 10,
                "TangentialLocation": 3,
                "Temperature": 86.02220198447681
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_10_4",
                "RadialLocation": 10,
                "TangentialLocation": 4,
                "Temperature": 85.9515730507539
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_10_5",
                "RadialLocation": 10,
                "TangentialLocation": 5,
                "Temperature": 85.62794879606703
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_10_6",
                "RadialLocation": 10,
                "TangentialLocation": 6,
                "Temperature": 85.1077416535532
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_10_7",
                "RadialLocation": 10,
                "TangentialLocation": 7,
                "Temperature": 84.5558460730979
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_10_8",
                "RadialLocation": 10,
                "TangentialLocation": 8,
                "Temperature": 84.38800116437093
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 85.15596999446525
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_11_1",
                "RadialLocation": 11,
                "TangentialLocation": 1,
                "Temperature": 85.46035435145062
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_11_2",
                "RadialLocation": 11,
                "TangentialLocation": 2,
                "Temperature": 85.77265228197048
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_11_3",
                "RadialLocation": 11,
                "TangentialLocation": 3,
                "Temperature": 85.9332393786103
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_11_4",
                "RadialLocation": 11,
                "TangentialLocation": 4,
                "Temperature": 85.86057652683503
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_11_5",
                "RadialLocation": 11,
                "TangentialLocation": 5,
                "Temperature": 85.54019891451838
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_11_6",
                "RadialLocation": 11,
                "TangentialLocation": 6,
                "Temperature": 85.02841898036823
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_11_7",
                "RadialLocation": 11,
                "TangentialLocation": 7,
                "Temperature": 84.48989158787563
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_11_8",
                "RadialLocation": 11,
                "TangentialLocation": 8,
                "Temperature": 84.34026508371804
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 85.0609586462242
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_12_1",
                "RadialLocation": 12,
                "TangentialLocation": 1,
                "Temperature": 85.33401494900832
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_12_2",
                "RadialLocation": 12,
                "TangentialLocation": 2,
                "Temperature": 85.62406465349571
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_12_3",
                "RadialLocation": 12,
                "TangentialLocation": 3,
                "Temperature": 85.77166667791926
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_12_4",
                "RadialLocation": 12,
                "TangentialLocation": 4,
                "Temperature": 85.69557555723651
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_12_5",
                "RadialLocation": 12,
                "TangentialLocation": 5,
                "Temperature": 85.38134620184415
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_12_6",
                "RadialLocation": 12,
                "TangentialLocation": 6,
                "Temperature": 84.88505340461238
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_12_7",
                "RadialLocation": 12,
                "TangentialLocation": 7,
                "Temperature": 84.37088482972203
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_12_8",
                "RadialLocation": 12,
                "TangentialLocation": 8,
                "Temperature": 84.25429268507521
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 84.92365713322249
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_13_1",
                "RadialLocation": 13,
                "TangentialLocation": 1,
                "Temperature": 85.15124970093335
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_13_2",
                "RadialLocation": 13,
                "TangentialLocation": 2,
                "Temperature": 85.40917370095498
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_13_3",
                "RadialLocation": 13,
                "TangentialLocation": 3,
                "Temperature": 85.53820467151863
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_13_4",
                "RadialLocation": 13,
                "TangentialLocation": 4,
                "Temperature": 85.45740348054949
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_13_5",
                "RadialLocation": 13,
                "TangentialLocation": 5,
                "Temperature": 85.15227089498245
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_13_6",
                "RadialLocation": 13,
                "TangentialLocation": 6,
                "Temperature": 84.67852137559639
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_13_7",
                "RadialLocation": 13,
                "TangentialLocation": 7,
                "Temperature": 84.19970227501898
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_13_8",
                "RadialLocation": 13,
                "TangentialLocation": 8,
                "Temperature": 84.13096264033555
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 84.74722753417352
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_14_1",
                "RadialLocation": 14,
                "TangentialLocation": 1,
                "Temperature": 84.91597661961154
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_14_2",
                "RadialLocation": 14,
                "TangentialLocation": 2,
                "Temperature": 85.1325925552967
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_14_3",
                "RadialLocation": 14,
                "TangentialLocation": 3,
                "Temperature": 85.23803535190785
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_14_4",
                "RadialLocation": 14,
                "TangentialLocation": 4,
                "Temperature": 85.15155065786486
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_14_5",
                "RadialLocation": 14,
                "TangentialLocation": 5,
                "Temperature": 84.85843840725663
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_14_6",
                "RadialLocation": 14,
                "TangentialLocation": 6,
                "Temperature": 84.41394106649224
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_14_7",
                "RadialLocation": 14,
                "TangentialLocation": 7,
                "Temperature": 83.98086781535885
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_14_8",
                "RadialLocation": 14,
                "TangentialLocation": 8,
                "Temperature": 83.97395320465996
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 84.54129289794639
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_15_1",
                "RadialLocation": 15,
                "TangentialLocation": 1,
                "Temperature": 84.64058454976485
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_15_2",
                "RadialLocation": 15,
                "TangentialLocation": 2,
                "Temperature": 84.8088719285881
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_15_3",
                "RadialLocation": 15,
                "TangentialLocation": 3,
                "Temperature": 84.88719477648736
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_15_4",
                "RadialLocation": 15,
                "TangentialLocation": 4,
                "Temperature": 84.79470655346894
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_15_5",
                "RadialLocation": 15,
                "TangentialLocation": 5,
                "Temperature": 84.51627175894359
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_15_6",
                "RadialLocation": 15,
                "TangentialLocation": 6,
                "Temperature": 84.10653564145082
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_15_7",
                "RadialLocation": 15,
                "TangentialLocation": 7,
                "Temperature": 83.72752499624497
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_15_8",
                "RadialLocation": 15,
                "TangentialLocation": 8,
                "Temperature": 83.7933977625181
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 84.32857921422408
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_16_1",
                "RadialLocation": 16,
                "TangentialLocation": 1,
                "Temperature": 84.35462756406618
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_16_2",
                "RadialLocation": 16,
                "TangentialLocation": 2,
                "Temperature": 84.4724525482866
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_16_3",
                "RadialLocation": 16,
                "TangentialLocation": 3,
                "Temperature": 84.523166059059
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_16_4",
                "RadialLocation": 16,
                "TangentialLocation": 4,
                "Temperature": 84.42552968094736
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_16_5",
                "RadialLocation": 16,
                "TangentialLocation": 5,
                "Temperature": 84.16369511341286
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_16_6",
                "RadialLocation": 16,
                "TangentialLocation": 6,
                "Temperature": 83.79148059751115
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_16_7",
                "RadialLocation": 16,
                "TangentialLocation": 7,
                "Temperature": 83.46994297305186
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_16_8",
                "RadialLocation": 16,
                "TangentialLocation": 8,
                "Temperature": 83.6121919126129
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 84.15458638641489
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_17_1",
                "RadialLocation": 17,
                "TangentialLocation": 1,
                "Temperature": 84.11702580410835
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_17_2",
                "RadialLocation": 17,
                "TangentialLocation": 2,
                "Temperature": 84.19108365006812
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_17_3",
                "RadialLocation": 17,
                "TangentialLocation": 3,
                "Temperature": 84.21875246419042
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_17_4",
                "RadialLocation": 17,
                "TangentialLocation": 4,
                "Temperature": 84.11858835846259
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_17_5",
                "RadialLocation": 17,
                "TangentialLocation": 5,
                "Temperature": 83.87389431965792
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_17_6",
                "RadialLocation": 17,
                "TangentialLocation": 6,
                "Temperature": 83.53711311757043
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_17_7",
                "RadialLocation": 17,
                "TangentialLocation": 7,
                "Temperature": 83.2673906228706
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_17_8",
                "RadialLocation": 17,
                "TangentialLocation": 8,
                "Temperature": 83.47512161521786
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 84.09149598499363
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_18_1",
                "RadialLocation": 18,
                "TangentialLocation": 1,
                "Temperature": 84.01960780282798
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_18_2",
                "RadialLocation": 18,
                "TangentialLocation": 2,
                "Temperature": 84.06841823558796
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_18_3",
                "RadialLocation": 18,
                "TangentialLocation": 3,
                "Temperature": 84.08372921202674
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_18_4",
                "RadialLocation": 18,
                "TangentialLocation": 4,
                "Temperature": 83.9853869947903
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_18_5",
                "RadialLocation": 18,
                "TangentialLocation": 5,
                "Temperature": 83.75620083790936
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_18_6",
                "RadialLocation": 18,
                "TangentialLocation": 6,
                "Temperature": 83.44622348918503
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_18_7",
                "RadialLocation": 18,
                "TangentialLocation": 7,
                "Temperature": 83.21015206714334
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "RotorWinding-Leading_Core_9_18_8",
                "RadialLocation": 18,
                "TangentialLocation": 8,
                "Temperature": 83.45122745564875
            }
        ],
        [
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 109.43639779394294
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 111.58064831341812
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 112.33673075883897
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 112.61734881241539
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 112.72517139105463
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 112.76757822511172
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 112.78452389936734
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 112.79136709843354
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 112.79414129035482
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 112.7952439826763
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 112.7956146528503
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 112.79519219360608
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 112.79437727768146
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 112.79211529593657
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 112.78650734630963
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 112.7728068761352
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 112.73928749125992
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 112.65681644179574
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 112.45214403786322
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_19_0",
                "RadialLocation": 19,
                "TangentialLocation": 0,
                "Temperature": 111.9376059314362
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_20_0",
                "RadialLocation": 20,
                "TangentialLocation": 0,
                "Temperature": 110.61817099064477
            },
            {
                "AxialCoordinate": 0.01225,
                "Name": "StatorWinding_Core_0_21_0",
                "RadialLocation": 21,
                "TangentialLocation": 0,
                "Temperature": 107.12730882191077
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 110.93881519323534
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 111.8630567944866
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 112.32786068335992
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 112.53410631699508
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 112.62168890857005
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 112.65826539740871
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 112.67344891693972
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 112.67973838707441
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 112.68233337900821
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 112.6833774556377
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 112.68373084405121
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 112.68331966157595
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 112.68253496451302
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 112.68036678667346
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 112.67502763700865
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 112.66210574366258
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 112.63090554035831
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 112.5556100207391
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 112.37424071720544
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_19_0",
                "RadialLocation": 19,
                "TangentialLocation": 0,
                "Temperature": 111.94002577982641
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_20_0",
                "RadialLocation": 20,
                "TangentialLocation": 0,
                "Temperature": 110.91737248276807
            },
            {
                "AxialCoordinate": 0.03675,
                "Name": "StatorWinding_Core_1_21_0",
                "RadialLocation": 21,
                "TangentialLocation": 0,
                "Temperature": 108.60920185887039
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 111.6055976799571
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 112.27784779267182
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 112.60911581842991
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 112.76352142725185
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 112.83271824765517
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 112.86296892777386
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 112.87599199340588
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 112.88154204271599
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 112.88388285041742
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 112.8848402180011
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 112.88516748244746
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 112.8847775437985
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 112.88404335155215
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 112.8820283495502
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 112.87711361512628
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 112.86536387068729
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 112.83742595659092
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 112.77127736321884
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 112.61560370154818
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_19_0",
                "RadialLocation": 19,
                "TangentialLocation": 0,
                "Temperature": 112.2526731676877
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_20_0",
                "RadialLocation": 20,
                "TangentialLocation": 0,
                "Temperature": 111.41827340621799
            },
            {
                "AxialCoordinate": 0.06125,
                "Name": "StatorWinding_Core_2_21_0",
                "RadialLocation": 21,
                "TangentialLocation": 0,
                "Temperature": 109.53371456903918
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 112.092946901836
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 112.73302856296507
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 113.02359396365723
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 113.15525754361632
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 113.21425778690089
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 113.24036582415283
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 113.25178992180048
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 113.25674011710575
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 113.25885989376158
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 113.25973793859409
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 113.26004077324323
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 113.25967956957138
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 113.25900267678551
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 113.25715648822276
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 113.25269178928808
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 113.24212403663431
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 113.21726897531308
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 113.15906796452293
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 113.02343319458147
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_19_0",
                "RadialLocation": 19,
                "TangentialLocation": 0,
                "Temperature": 112.70900360841472
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_20_0",
                "RadialLocation": 20,
                "TangentialLocation": 0,
                "Temperature": 111.98359387521305
            },
            {
                "AxialCoordinate": 0.08574999999999999,
                "Name": "StatorWinding_Core_3_21_0",
                "RadialLocation": 21,
                "TangentialLocation": 0,
                "Temperature": 110.31331018346162
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 112.55702476845967
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 113.21871432692204
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 113.50637523182537
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 113.63254990164965
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 113.68803161589443
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 113.71238242343271
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 113.72302445843454
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 113.72764838154339
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 113.72963765892489
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 113.73046596788893
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 113.73075332651867
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 113.73042510148184
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 113.72980114980143
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 113.72810623853344
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 113.72403033495927
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 113.71444023619996
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 113.6920093063723
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 113.63970829062274
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 113.51804693690255
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_19_0",
                "RadialLocation": 19,
                "TangentialLocation": 0,
                "Temperature": 113.23544789439157
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_20_0",
                "RadialLocation": 20,
                "TangentialLocation": 0,
                "Temperature": 112.57891063839902
            },
            {
                "AxialCoordinate": 0.11024999999999999,
                "Name": "StatorWinding_Core_4_21_0",
                "RadialLocation": 21,
                "TangentialLocation": 0,
                "Temperature": 111.04979634932388
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 113.02487526172119
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 113.72388727424615
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 114.02377894375459
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 114.15337803586739
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 114.20959881430493
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 114.23400640275325
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 114.24458746853632
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 114.24915925020612
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 114.251119074536
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 114.25193373939435
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 114.25221711962928
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 114.25192263183413
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 114.25134066391506
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 114.24976182536238
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 114.24597402257126
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 114.23708220112384
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 114.2163214255417
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 114.16796046269305
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 114.05544788455045
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_19_0",
                "RadialLocation": 19,
                "TangentialLocation": 0,
                "Temperature": 113.79373586100627
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_20_0",
                "RadialLocation": 20,
                "TangentialLocation": 0,
                "Temperature": 113.18419413089612
            },
            {
                "AxialCoordinate": 0.13474999999999998,
                "Name": "StatorWinding_Core_5_21_0",
                "RadialLocation": 21,
                "TangentialLocation": 0,
                "Temperature": 111.7602090708376
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 113.49018936041679
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 114.23495368679114
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 114.55607732632879
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 114.69483682354671
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 114.75473079253595
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 114.78052352947358
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 114.79160103528557
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 114.79634308003085
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 114.79835903231759
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 114.79919174486437
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 114.79948140989539
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 114.79921815337086
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 114.79866481201621
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 114.79716156272922
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 114.79355268588844
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 114.78507371017716
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 114.76525714054387
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 114.71905773197447
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 114.61156588157
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_19_0",
                "RadialLocation": 19,
                "TangentialLocation": 0,
                "Temperature": 114.36188971469898
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_20_0",
                "RadialLocation": 20,
                "TangentialLocation": 0,
                "Temperature": 113.78246207050485
            },
            {
                "AxialCoordinate": 0.15925,
                "Name": "StatorWinding_Core_6_21_0",
                "RadialLocation": 21,
                "TangentialLocation": 0,
                "Temperature": 112.43624036878533
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 113.92992555065108
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 114.73786485857674
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 115.09336715609057
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 115.24767701267746
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 115.31391790041454
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 115.34214555628304
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 115.3541200174156
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 115.35918305021274
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 115.36131132746515
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 115.3621825899001
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 115.3624850258892
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 115.36224772597363
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 115.36171046487806
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 115.36024580879618
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 115.35671761100198
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 115.3483948744065
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 115.32885713688658
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 115.28311269035291
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 115.17636036180865
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_19_0",
                "RadialLocation": 19,
                "TangentialLocation": 0,
                "Temperature": 114.92847290993811
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_20_0",
                "RadialLocation": 20,
                "TangentialLocation": 0,
                "Temperature": 114.35701714090926
            },
            {
                "AxialCoordinate": 0.18375,
                "Name": "StatorWinding_Core_7_21_0",
                "RadialLocation": 21,
                "TangentialLocation": 0,
                "Temperature": 113.05097985588071
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 114.27757368923403
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 115.21945192057917
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 115.63871893033131
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 115.81753088884126
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 115.89256354215114
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 115.92386639147274
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 115.93690569035437
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 115.94233564175899
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 115.94458982721694
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 115.94550392468904
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 115.9458201843683
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 115.94560141861297
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 115.94507086656228
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 115.94361819952601
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 115.9401011174926
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 115.9317501964968
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 115.9119831642551
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 115.8652239565983
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 115.75476480405969
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_19_0",
                "RadialLocation": 19,
                "TangentialLocation": 0,
                "Temperature": 115.49494835732253
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_20_0",
                "RadialLocation": 20,
                "TangentialLocation": 0,
                "Temperature": 114.89091078451081
            },
            {
                "AxialCoordinate": 0.20825,
                "Name": "StatorWinding_Core_8_21_0",
                "RadialLocation": 21,
                "TangentialLocation": 0,
                "Temperature": 113.52853593443058
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_0_0",
                "RadialLocation": 0,
                "TangentialLocation": 0,
                "Temperature": 114.30135484474161
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_1_0",
                "RadialLocation": 1,
                "TangentialLocation": 0,
                "Temperature": 115.69630600319486
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_2_0",
                "RadialLocation": 2,
                "TangentialLocation": 0,
                "Temperature": 116.22722808572601
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_3_0",
                "RadialLocation": 3,
                "TangentialLocation": 0,
                "Temperature": 116.4356884859229
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_4_0",
                "RadialLocation": 4,
                "TangentialLocation": 0,
                "Temperature": 116.51914972457158
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_5_0",
                "RadialLocation": 5,
                "TangentialLocation": 0,
                "Temperature": 116.55298894119376
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_6_0",
                "RadialLocation": 6,
                "TangentialLocation": 0,
                "Temperature": 116.56682547050002
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_7_0",
                "RadialLocation": 7,
                "TangentialLocation": 0,
                "Temperature": 116.57251384163476
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_8_0",
                "RadialLocation": 8,
                "TangentialLocation": 0,
                "Temperature": 116.57485345178638
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_9_0",
                "RadialLocation": 9,
                "TangentialLocation": 0,
                "Temperature": 116.57579596669432
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_10_0",
                "RadialLocation": 10,
                "TangentialLocation": 0,
                "Temperature": 116.57612120476709
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_11_0",
                "RadialLocation": 11,
                "TangentialLocation": 0,
                "Temperature": 116.57591208097477
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_12_0",
                "RadialLocation": 12,
                "TangentialLocation": 0,
                "Temperature": 116.57538321633822
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_13_0",
                "RadialLocation": 13,
                "TangentialLocation": 0,
                "Temperature": 116.57393060133587
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_14_0",
                "RadialLocation": 14,
                "TangentialLocation": 0,
                "Temperature": 116.57039926660535
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_15_0",
                "RadialLocation": 15,
                "TangentialLocation": 0,
                "Temperature": 116.5619660814001
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_16_0",
                "RadialLocation": 16,
                "TangentialLocation": 0,
                "Temperature": 116.54183754532554
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_17_0",
                "RadialLocation": 17,
                "TangentialLocation": 0,
                "Temperature": 116.49362213461924
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_18_0",
                "RadialLocation": 18,
                "TangentialLocation": 0,
                "Temperature": 116.3774247118225
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_19_0",
                "RadialLocation": 19,
                "TangentialLocation": 0,
                "Temperature": 116.09471568546068
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_20_0",
                "RadialLocation": 20,
                "TangentialLocation": 0,
                "Temperature": 115.39622010173571
            },
            {
                "AxialCoordinate": 0.23274999999999998,
                "Name": "StatorWinding_Core_9_21_0",
                "RadialLocation": 21,
                "TangentialLocation": 0,
                "Temperature": 113.62551889663209
            }
        ]
    ]

    # jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
    # json_component = jsonpickle.encode(component_temperatures, unpicklable=False)
    # json_winding = jsonpickle.encode(winding_temperatures, unpicklable=False)

    res_dic = {
        "component_temperatures": component_temperatures,
        "winding_temperatures": winding_temperatures
    }
    return Response(res_dic)
