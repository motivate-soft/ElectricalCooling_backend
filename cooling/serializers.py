from rest_framework import serializers

from accounts.serializers import UserRegistrationSerializer
from cooling.models import Cooling


class CoolingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooling
        fields = ('id', 'name', 'components', 'losses', 'faces', 'passages', 'fluids', 'owner')
        read_only_fields = ()

    def to_representation(self, instance):
        self.fields['owner'] = UserRegistrationSerializer(read_only=True)
        return super(CoolingSerializer, self).to_representation(instance)
