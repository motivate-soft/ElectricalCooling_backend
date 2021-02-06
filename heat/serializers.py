from rest_framework import serializers

from heat.models import Cooling


class CoolingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooling
        fields = ('components', 'losses', 'faces', 'passages', 'fluids')
