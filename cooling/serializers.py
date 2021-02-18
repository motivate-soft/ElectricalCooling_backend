from rest_framework import serializers

from cooling.models import Cooling


class CoolingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooling
        fields = ('name', 'components', 'losses', 'faces', 'passages', 'fluids', 'owner')
